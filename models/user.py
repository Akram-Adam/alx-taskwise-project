''' Module for user '''
import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey\
    , Table, DateTime, Boolean
from sqlalchemy import CHAR, DateTime, func
from models.extra.extrafile import is_list_part_of
from models.base_model import BaseModel, Base
from models.engine.Errorevent import ERROR_EVENT
import bcrypt



class User(BaseModel, Base):
    """ User class """
    __tablename__ = 'users'
    username = Column(String(256), unique=True, nullable=False)
    email= Column(String(256), unique=True, nullable=False)
    user_password = Column(String(256), nullable=False)
    gender = Column(CHAR(1), nullable=True)
    birthdate = Column(DateTime, nullable=True)
    frist_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    Account_valid = Column(Boolean, nullable=False,default=False)

    def __init__(self, *args, **kwargs):
        """ calss constructor don't use it outside the class for security """
        print('um here User Constructor')
        self.__set_password(kwargs['user_password'])
        del  kwargs['user_password']
        super().__init__(*args, **kwargs)
    
    @classmethod
    def create(cls, *args, **kwargs):

        """
            create a new user don't
            use the calss constuctor
            outside the class for security
            requrment to create the instance
            - username
            - email
            - user_password
            - conforming_password
        """

        # Check if the password validation
        # Check email
        # Check username
        # Check if the user already exist
    
        if kwargs['email'] and kwargs['username']:
            check = cls.__check_email_and_username(email=kwargs['email'], username=kwargs['username'])
            if isinstance(check, ERROR_EVENT):
                return check
        else:
            return ERROR_EVENT(maasage=" importand data is missing ", code='1.0.0', typeevent='Usererror')
        if kwargs["user_password"] and kwargs["conformingpassword"]:
            check = cls.__check_password_validation(password=kwargs['user_password'], conformingpassword=kwargs['conformingpassword'])
            if isinstance(check, ERROR_EVENT):
                return check
        else:
            return ERROR_EVENT(maasage=" password or conforming password is missing ", code='1.0.1', typeevent='Usererror')
        if kwargs['conformingpassword']:
            del kwargs['conformingpassword']
            
            new_user = cls(*args, **kwargs)
            print(new_user)
            
        return new_user

    def __set_password(self, password):
        """
        Hash the password and store it.
        """
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        self.user_password = hashed_password.decode('utf-8')

    def verify_password(self, password):
        """
        Verify the provided password against the stored hashed password.
        """
        return bcrypt.checkpw(password.encode('utf-8'), self.user_password.encode('utf-8'))

    def __check_password_validation(password, conformingpassword):
        """ Function to check the password if it valed to be a password or Not """
        SpecialSym = ['!', '@', '#', '"', ':', "'", '<', '>', ',', '\\', '/', '$', '%'
                      , '^', '&', '*', '(', ')', '{', '}' ,
                      '[', ']', '_', '+', '-', '=', '|', ';', '.', '?', '`', '~']

        # Check the lengnth of the password
        if not (len(password) >= 8 and len(password) < 61):
            return ERROR_EVENT(maasage=" The password length is out of the range ", code='1.1.0', typeevent='Usererror')
    
        # Check if the password has Number
        if not any(char.isdigit() for char in password):
            return ERROR_EVENT(maasage=" No digits ", code='1.1.1', typeevent='Usererror')

        # Check if there is any uppercases in the password
        if not any(char.isupper() for char in password):
            return ERROR_EVENT(maasage=" No upper letters ", code='1.1.2', typeevent='Usererror')

        # Check if there is any lowercase in the password
        if not any(char.islower() for char in password):
            return ERROR_EVENT(maasage=" No small letter ", code='1.1.3', typeevent='Usererror')

        # Check if there is any
        if not any(char in SpecialSym for char in password):
            return ERROR_EVENT(maasage=" No symbol ", code='1.1.4', typeevent='Usererror')

        # Check if the password and conforming password
        if password != conformingpassword:
            return ERROR_EVENT(maasage=" Password Dosn't match conforming password ", code='1.1.4', typeevent='Usererror')

        return True

    def __check_email_and_username(email=None, username=None):
        """
            Check if the email is exist
            return True: if user and email are valid and no matched
            return ERROR_event: if user is exist
        """
        from models import dp_incetnace
        check_data = dp_incetnace.account_check_existance(email, username)
        if check_data:
            if check_data[0] == True or check_data[1] == True:
                return ERROR_EVENT(maasage=" The Account is exist ", code='1.2.0', typeevent='Usererror')
            if check_data[0] is None and check_data[1] is None: # 
                return ERROR_EVENT(maasage=" Data is missing ", code='1.2.1', typeevent='Usererror') 
            if email:
                if not (len(email) > 0 and len(email) < 256):
                    return ERROR_EVENT(maasage=" The email length is Out of the range ", code='1.2.2', typeevent='Usererror')
            if username:
                if not (len(username) > 0 and len(username) < 256):
                    return ERROR_EVENT(maasage=" The username length is Out of the range ", code='1.2.3', typeevent='Usererror')
        return True

    @staticmethod
    def log_in_check(username_or_email, password):
        """
        Check if the user is exist and the password is write
        return the user if the data is right
        return user object or return None if the password
        is wrong or the user is not exist
        """
        from models import dp_incetnace
        user = dp_incetnace.getuser(username_or_email)
        if user:
            if user:
                if user.verify_password(password):
                    return user
        return None
