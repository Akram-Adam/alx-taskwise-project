"""
  This module for category
- There are two sprated type for category
- Frist: category for tasks
- secand: category for expencises
"""
from models.base_model import BaseModel, Base
from models.base_model import Base, BaseModel
from datetime import datetime
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey\
    , Table, DateTime, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy import CHAR, DateTime, func
from models.engine.Errorevent import ERROR_EVENT


class Category_tasks(BaseModel, Base):
    """ This class for category of tasks """
    __tablename__ = 'category_tasks'
    name = Column(String(128), nullable=False, unique=True)
    description = Column(String(1024), nullable=True)
    
    # The Relation between the tasks and the categories
    tasks = relationship('Task', backref='Category_task', cascade='all, delete-orphan')
    
    # The relationship between tasks-category and the panels
    panel_id = Column(ForeignKey('panels.id'), nullable=False)

    
    def __init__(*args, **kwargs):
        """ This method for init the category """
        super().__init__(*args, **kwargs)

    def create(self, *args, **kwargs):
        """ This method for create a new category """
        if not kwargs['name']:
            """ Data missing """
            return ERROR_EVENT(maasage="Name feild is missing", code='3.1.0', typeevent='Usererror')
        else:
            # check if there is any Category by the name
            from models import dp_incetnace
            instance_ = dp_incetnace.get_data('Category_tasks', f'name={kwargs["name"]}')

            if instance_.count() > 0:
                return ERROR_EVENT(maasage="Category already exist", code='3.1.3', typeevent='Usererror')
    
        if not kwargs['description']:
            return ERROR_EVENT(maasage="Description feild is missing", code='3.1.1', typeevent='Usererror')
        if not kwargs['panel_id']:
            return ERROR_EVENT(massage="The panel_id feild is missing", code='3.1.2', typeevent='Usererror')    

        return self.__init__(*args, **kwargs)

    
        
class Category_expencics(BaseModel, Base):
    """ This class for category of expense """
    __tablename__ = 'category_expenses'
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)

    # The relationship between Category_expencics and panle
    panel_id = Column(ForeignKey('panels.id'), nullable=False)

    # The relationship between Category_expencics and expense
    expenses = relationship('Expense', backref='Category_expenses', cascade='all, delete-orphan')


    def __init__(self, *args, **kwargs):
        """ This method for init the category """
        super().__init__(*args, **kwargs)

    @classmethod
    def create(cls, *args, **kwargs):
        """ This method for create a new category """
        if not kwargs['name'] or kwargs['name'] == '':
            """ Data missing """
            return ERROR_EVENT(maasage="Name feild is missing", code='4.1.0', typeevent='Usererror')
    
        if not kwargs['description']:
            return ERROR_EVENT(maasage="Description feild is missing", code='4.1.1', typeevent='Usererror')
        
        if (not kwargs['panel_id']) or kwargs['panel_id'] == '':
            return ERROR_EVENT(massage="The panel_id feild is missing", code='4.1.3', typeevent='Usererror')

        return cls(*args, **kwargs)
