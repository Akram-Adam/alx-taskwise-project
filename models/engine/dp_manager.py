"""module for manage the database"""
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.sql import select, insert, update, delete, exists
from sqlalchemy import CHAR, DateTime, func
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy import or_, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import NoSuchTableError, OperationalError, ProgrammingError
# Class models
from models.extra.extrafile import get_Config_data
from models.engine.Errorevent import ERROR_EVENT

from models.base_model import BaseModel, Base
from models.user import User
# from models.budget import
from models.category import Category_expencics, Category_tasks
from models.expense import Expense
from models.task import Task, TimedTask, Dailytasks
from models.panel import Panel, UserPanel


class DBStorage:
    """ Class that handel the datatbase """
    __engine = None
    __session = None
     
    def __init__(self):
        """ Constructor of the class make instance database"""
        configdata= get_Config_data('config.txt')
            

        mysql_user = configdata['dpuser']
        mysql_pwd = configdata['dpuserpass']
        mysql_host = configdata['host']
        mysql_db = configdata['dp']
        mysqlmood = configdata['mood']

        # Construct the database URL
        # should change it after tested
        db_url = f"mysql+mysqldb://{mysql_user}:{mysql_pwd}@{mysql_host}/{mysql_db}"

        # Create the engine
        self.__engine = create_engine(db_url, pool_pre_ping=True)

        # Create a sessionmaker
        Session = sessionmaker(bind=self.__engine)

        # Create a session
        self.__session = Session()

        # if mysqlmood == 'test':
        #     print('all data have been deleted befor start')
        #     Base.metadata.drop_all(self.__engine)
            
    def clean_for_testing(self,test=True):
        if test:
            Base.metadata.drop_all(self.__engine)

    def rollback(self):
        self.__session.rollback()

    def all(self, cls=None):
        """
        this method must return a dictionary
        key = <class-name>.<object-id>
        value = object
        """
        
        data = {}
        if self.__session.is_active: #check if the session is open
            try:
                """
                if cls:  #check  if class was passed to method
                    
                    objects = self.__session.query(cls).all()
                    for obj in objects:
                        key = "{}.{}".format(obj.__class__.__name__, obj.id)
                        data[key] = obj
                else:
                    # Retrieve all objects from all classes
                    objects = self.__session.query(State).all() + \
                        self.__session.query(City).all() + \
                        self.__session.query(User).all() + \
                        self.__session.query(Place).all() + \
                        self.__session.query(Amenity).all() + \
                        self.__session.query(Review).all()
                    for obj in objects:
                        key = "{}.{}".format(obj.__class__.__name__, obj.id)
                        data[key] = obj
                    """

            except NoSuchTableError as no_table:  #incase we wanna test where the error
                pass
            except OperationalError as OP_Error:
                pass
            except ProgrammingError as API_Error:
                pass
        return data

    def new(self, obj):
        """ add the object to the current database session """
        if obj is not None:
            if self.__session.is_active:  #check if the session is open
                try:
                    self.__session.add(obj)
                except NoSuchTableError as no_table:  #incase we wanna test where the error
                    pass
                except OperationalError as OP_Error:
                    pass
                except ProgrammingError as API_Error:
                    pass
             
    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """"delete from the current database session obj if not None"""
        if obj is not None:
            if self.__session.is_active:  #check if the session is open
                try:
                    self.__session.delete(obj)
                    print("Object deleted successfully.")
                    self.__session.commit()
                except NoSuchTableError as no_table:  #incase we wanna test where the error
                    pass
                except OperationalError as OP_Error:
                    pass
                except ProgrammingError as API_Error:
                    pass

    def reload(self):
        """
        Create all tables in the database and create a new session.
        """
        # Create all tables in the database
        Base.metadata.create_all(self.__engine)

        # Create a sessionmaker with scoped_session
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

        try:
            # Attempt to commit any pending transactions
            self.__session.commit()
        except OperationalError:
            # Handle operational errors if any
            pass

    def account_check_existance(self, email=None, username=None):
        """
            Method to check to check if there user by same username or same email
                - check email if is not None
                - check username if is not None
                return tuble (True, True) / (False, False)
        """
        emailres= None
        usernameres= None
        if email:
            q_statment = exists().where(User.email == email)
            if self.__session.is_active:
                emailres = self.__session.query(q_statment).scalar()
    
        if username:
            if self.__session.is_active:
                q_statment = exists().where(User.username == username)
                usernameres = self.__session.query(q_statment).scalar()

        return (emailres, usernameres)

    def getuser(self, usernameoremail):
        """ Get user object """
        if self.__session.is_active: #check if the session is open
            try:
                if usernameoremail: # Check if and 
                    objects = self.__session.query(User).filter(or_(User.username == usernameoremail, User.email == usernameoremail)).first()
                    return objects

            except NoSuchTableError as no_table:  #incase we wanna test where the error
                return
            except OperationalError as OP_Error:
                pass
            except ProgrammingError as API_Error:
                pass
        return

    def close(self):
        """ Close the session """
        self.__session.rollback()  # In case there's a pending transaction
        self.__session.close()     # Cl
    
    def get_data(self, class_name, attrib):
        """
        Method to return instances by attribute.
        :param class_name: str  :: Name of the class to query
        :param attrib: str  :: Attribute in the format attribute=value
        :return: Instance that matches the attribute condition, or None if not found
        """
        # Mapping of class names to class objects
        classes = {
            'User': User,
            'Category_expencics': Category_expencics,
            'Category_tasks': Category_tasks,
            'Expense': Expense,
            'Task': Task,
            'TimedTask': TimedTask,
            'Dailytasks': Dailytasks,
            'Panel': Panel,
            'UserPanel': UserPanel
        }

        if class_name in classes:
            if attrib:
                # Split the attribute into key and value
                attribute_data = attrib.split('=')
                if len(attribute_data) != 2:
                    raise ValueError("Attribute must be in the format 'attribute=value'")

                attribute_name, attribute_value = attribute_data

                # Ensure the class has the requested attribute
                model_class = classes[class_name]
                if hasattr(model_class, attribute_name):
                    # Dynamically build the query
                    objects = self.__session.query(model_class).filter(
                        getattr(model_class, attribute_name) == attribute_value
                    )
                    return objects
                else:
                    raise AttributeError(f"{class_name} has no attribute '{attribute_name}'")
        else:
            raise ValueError(f"Class '{class_name}' not found in available classes.")