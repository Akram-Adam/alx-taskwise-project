""" module for Tasks class"""

from models.base_model import Base, BaseModel
from datetime import datetime
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey\
    , Table, DateTime, Boolean
from sqlalchemy import CHAR, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from datetime import datetime, timedelta
from models.engine.Errorevent import ERROR_EVENT


class Task(BaseModel, Base):
    """Task class inherits from BaseModel and Base"""
    __tablename__ = 'tasks'
    title = Column(String(128),nullable=False, unique=False)
    description = Column(String(1024), nullable=True)

    # Status : True for valid 
    status = Column(Boolean, default=True, nullable=False)
    completed = Column(Boolean, default=False, nullable=False)

    # relationship
    category_id = Column(String(60), ForeignKey('category_task.id'), nullable=False)
    notification_time = Column(DateTime, nullable=True)

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'task'
    }

    def __init__(self, *args, **kwargs):
        """ This is the constructor of the calss """
        super().__init__(*args, **kwargs)
        


class Dailytasks(Task):
    """Dailytasks class inherits from Task"""
    daily_time = Column(DateTime, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'daily'
    }

    def __init__(self, *args, **kwargs):
        """ This is the constructor of the calss """
        super().__init__(*args, **kwargs)

    def create(cls, *args, **kwargs):
        from models import dp_incetnace
        # Add validation logic here (e.g., checking for required arguments)
        if 'daily_time' not in kwargs:
            return ERROR_EVENT(maasage=" start_time is required for TimedTask ", code='6.1.1', typeevent='Usererror')
        if kwargs['title']: # insure the uniqeness of the title
            check  = dp_incetnace.get_data('Task', f'title={kwargs['title']}')
            if len(check) > 0:
                return  ERROR_EVENT(maasage=" Task with this title already exists ", code='6.1.4', typeevent='Usererror') 
        else:
            return ERROR_EVENT(maasage=" 'titel' is missing", code='6.1.4', typeevent='Usererror')
        if not kwargs['category_id']:
            return ERROR_EVENT(maasage=" 'category_id' is missing", code='6.1.5', typeevent='Usererror')
        
        return cls(*args, **kwargs)





class TimedTask(Task):
    start_time = Column(DateTime, nullable=True, default=datetime.utcnow())
    end_time = Column(DateTime, nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'timed'
    }

    def __init__(self, *args, **kwargs):
        """Constructor for TimedTask class"""
        super().__init__(*args, **kwargs)


    def create(cls,*args, **kwargs):
        """Create method to check inputs before calling the constructor"""
        
        from models import dp_incetnace
        # Add validation logic here (e.g., checking for required arguments)
        if 'start_time' not in kwargs:
            return ERROR_EVENT(maasage=" start_time is required for TimedTask ", code='5.1.1', typeevent='Usererror')

        if  'end_time' not in kwargs:
            return ERROR_EVENT(maasage=" end_time is required for TimedTask ", code='5.1.2', typeevent='Usererror')
         # First, check input data (like ensuring the start_time is before end_time)

        if kwargs['start_time'] >= kwargs['end_time']:
               return ERROR_EVENT(maasage=" End time must be after start time ", code='5.1.3', typeevent='Usererror')
    
        if kwargs['title']:
            check  = dp_incetnace.get_data('Task', f'title={kwargs['title']}')
            if len(check) > 0: # check if there is any task by the same titel
                return ERROR_EVENT(maasage=" Task with this title already exists ", code='5.1.4', typeevent='Usererror') 
        else:
            return ERROR_EVENT(maasage=" 'titel' is missing ", code='5.1.4', typeevent='Usererror')
    
        if not kwargs['category_id']:
            return ERROR_EVENT(maasage=" 'category_id' is missing ", code='5.1.5', typeevent='Usererror')
        # If all checks pass, call the constructor
      
        # Call the Task constructor (super constructor)
        return cls(*args, **kwargs)


    # Calculate the default notification time based on the start time
    def calculate_default_notification_time(self, minutes_before_start=30):
        if self.start_time:
            self.notification_time = self.start_time - timedelta(minutes=minutes_before_start)
