""" moudels for expencies """

from models.base_model import Base, BaseModel
from datetime import datetime
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey\
    , Table, DateTime, Boolean, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy import CHAR, DateTime, func
from models.engine.Errorevent import ERROR_EVENT


class Expense(BaseModel, Base):
    """
    This calss for expense
    cateogry: id
    amount: float
    titel: string
    category: str
    description: str
    """
    title = Column(String(128), nullable=False, unique=True)
    description = Column(String(1024))
    amount = Column(Float, nullable=False)
    category_id = Column(String(60), ForeignKey('category_expenses.id'), nullable=True)
    
    
    def __init__(self, *args, **kwargs):
        """ This is the constructor of the calss"""
        super().__init__(*args, **kwargs)
        
    def create(cls, *args, **kwargs):
        """ Class to check if there is no missing data befor calling the Constructor """
        from models import dp_incetnace
        # Add validation logic here (e.g., checking for required arguments)
        if kwargs['title']: # insure the uniqeness of the title
            check  = dp_incetnace.get_data('Task', f'title={kwargs['title']}')

            if len(check) > 0:
                return  ERROR_EVENT(maasage=" Task with this title already exists ", code='7.1.0', typeevent='Usererror') 
        else:
            return ERROR_EVENT(maasage=" 'titel' is missing ", code='7.1.1', typeevent='Usererror')
        
        if kwargs['amount']: # insure the amoun in the data
            if (kwargs['amount']).isdigit():
                kwargs['amount'] = float(kwargs['amount'])
            else:
                 return ERROR_EVENT(maasage=" 'amount' must be digit ", code='7.1.2', typeevent='Usererror')
        else:
            return ERROR_EVENT(maasage=" 'amount' is missing", code='7.1.3', typeevent='Usererror')
        
        if not kwargs['category_id']:
            return ERROR_EVENT(maasage=" 'category_id' is missing ", code='7.1.4', typeevent='Usererror')
        
        return cls(*args, **kwargs)
