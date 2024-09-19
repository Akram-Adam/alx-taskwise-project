#!/usr/bin/python3
'''
    This module conntain the base_model of the all classes
    written by mahmoud Adam
    email: mahmoudadam5555@gmail.com
'''
import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy import CHAR, DateTime,func
from sqlalchemy.orm import declarative_base
from models.extra.extrafile import is_list_part_of
# from models import dp_incetnace
from models.engine.Errorevent import ERROR_EVENT

Base = declarative_base()

class BaseModel:
    '''
    This is the base model of all classes "the interface calss"
    attributes: id - created_at - updated_at
    methods:  __init__ - __str__ - save - delete - update - to_dict - __repr__
    '''
    __abstract__ = True
    id = Column(String(60), primary_key=True,nullable=False,default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())


    def __init__(self, *args, **kwargs):
        """ The constructor of the class expect: dict() of data """
        print('um here in the base class')
        if 'id' not in kwargs:
            self.id = str(uuid.uuid4())
        if 'created_at' not in kwargs:
            self.created_at = datetime.utcnow()
        else:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
        if 'updated_at' not in kwargs:
            self.updated_at = self.created_at
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")

        if '__class__' in kwargs:
            del kwargs['__class__']

        if 'user_password' in kwargs:
            del kwargs['user_password']
        self.__dict__.update(kwargs)
        self.save()
    


    def __str__(self):
        """
        Represinting string of the class
        """
        obj_dict = (self.__dict__).copy()
        obj_dict.pop('_sa_instance_state', None)
        obj_dict.pop('user_passoword', None)

        if 'user_password' in obj_dict:
            del obj_dict['user_password']

        return '[{}] ({}) {}'.format(type(self).__name__, self.id, obj_dict)


    def save(self):
        """
        Update databse by the new element "Object"
        """
        from models import dp_incetnace
        dp_incetnace.new(self)
        dp_incetnace.save()


    def delete(self):
        """
        Delete the object from database
        """
        from models import dp_incetnace
        dp_incetnace.delete(self)


    def update(self, **kwargs):
        from models import dp_incetnace
        """ Method for update data attribute """
        if 'id' in kwargs:
            """ Drop The request """
            return ERROR_EVENT(maasage=" You can't update 'id' feild", code='0.5.0', typeevent='Usererror')

        if 'created_at' in kwargs:
            """ Drop The request """
            return ERROR_EVENT(maasage="You can't update 'created_at' feild", code='0.5.1', typeevent='Usererror')

        if 'updated_at' in kwargs:
            """ Drop The request """
            return ERROR_EVENT(maasage="You can't update 'updated_at' feild", code='0.5.2', typeevent='Usererror')

        if is_list_part_of(kwargs.keys(), __dict__.keys()):    
            self.__dict__.update(kwargs)
        else:
            return ERROR_EVENT(maasage="You can't update, data not compatible", code='0.5.3', typeevent='Usererror')

        dp_incetnace.save()


    def to_dict(self):
        """
        This function  it has no argumants and returns
        a dictionary containing all keys/values of __dict__ of the instance
        """
        obj_dict = {}
        for key, value in self.__dict__.items():
            if key not in ['created_at', 'updated_at']:
                obj_dict[key] = value
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        if 'user_password' in obj_dict:
            del obj_dict['user_password']

        return obj_dict

    def __repr__(self):
        """ The represintation of the object as string while printed """
        repdict = self.__dict__.copy()
        repdict.pop('_sa_instance_state', None)
        repdict.pop('user_passoword', None)
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, repdict)

