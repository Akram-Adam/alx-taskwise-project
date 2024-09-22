"""
The module for panel which table refer to 
domain access to the Users in said the panels
grouped accounts 

"""
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from models.user import User
from models.engine.Errorevent import ERROR_EVENT


class Panel(BaseModel, Base):
    __tablename__ = 'panels'
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)

    # Define relationship to users through the UserPanels table
    users = relationship('User', secondary='user_panels', back_populates='panels', overlaps="user_panels")
    user_panels = relationship('UserPanel', back_populates='panel',overlaps="users,panels", cascade="all, delete-orphan")

    # The relationship between Category_expencics and panle
    Category_expencics = relationship('Category_expencics', backref='panel', cascade="all, delete-orphan")

    # relationship between tasks_categorys and panels
    Category_tasks = relationship('Category_tasks', backref='panel', cascade="all, delete-orphan")
    # constructor

    def __init__(self, *args, **kwargs):
        """ The constructor of panel calss """
        super().__init__(*args, **kwargs)

    @classmethod  
    def create(cls, *args, **kwargs):
        """add check condition in the future"""
        from models import dp_incetnace
        if not kwargs['name'] or kwargs['name'] == '':
            return ERROR_EVENT(maasage=" Name is missing ", code='9.1.0', typeevent='Usererror')

        return cls(*args, **kwargs)


class UserPanel(BaseModel, Base):
    """
        the complex relation between the uaer and the panel which is
        every class have diffrace access level
    """
    __tablename__ = 'user_panels'
    user_id = Column(ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    panel_id = Column(ForeignKey('panels.id', ondelete='CASCADE'), primary_key=True)
    access_level = Column(String(32), nullable=False)  # Roles: 'owner', 'editor', 'viewer'

    # Relationships
    user = relationship('User', back_populates='user_panels', overlaps="panels,users")
    panel = relationship('Panel', back_populates='user_panels', overlaps="panels,users")
    
    def __init__(self, *args, **kwargs):
        """
        The constructor of the relationship
        """
        super().__init__(*args, **kwargs)

    @classmethod
    def create(cls, *args, **kwargs):
        """ check layer """
        if kwargs['user_id'] in [None, ''] or kwargs['panel_id'] in [None, ''] :
            return ERROR_EVENT(maasage=" 'user_id' or 'panel_id' is missing ", code='8.1.0', typeevent='Usererror')
        if not kwargs['access_level']:
            return ERROR_EVENT(maasage=" 'access_level' is missing ", code='8.1.1', typeevent='Usererror')
        else:
            if kwargs['access_level'] not in ['owner', 'editor', 'viewer']:
                return ERROR_EVENT(maasage="Invalid access level", code='8.1.2', typeevent='Usererror')

        # create instance
        return cls(*args, **kwargs)
