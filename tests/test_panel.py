""" 
testing module for panle
create
delete
update
"""


import unittest
from models.user import User
from models.panel import Panel, UserPanel
from models.engine.Errorevent import ERROR_EVENT
from models.engine.dp_manager import DBStorage
from models.engine.Errorevent import ERROR_EVENT
import uuid
import bcrypt
from sqlalchemy.exc import IntegrityError


class Testpanle(unittest.TestCase):
    """ Test cases for User class """
    @classmethod
    def setUpClass(cls):
        """ Set up for the tests. Initialize DBStorage """
        #cls.storage = DBStorage()
        #cls.storage.reload() # Reload database/tables
        from models import dp_incetnace
        cls.storage = dp_incetnace
        cls.storage.reload()

    @classmethod
    def tearDownClass(cls):
        """ Clean up after tests """
        cls.storage.rollback()
        cls.storage.close()  # Ensure the session is properly closed
        
    def setUp(self):
        """ Set up an initial user before each test """
        self.username = f"testuser_{uuid.uuid4()}"
        self.email = f"testuser_{uuid.uuid4()}@example.com"
        self.user = User.create(username=self.username, email=self.email\
            , user_password="1123122testpassword@Mahmoud",\
                conformingpassword="1123122testpassword@Mahmoud")
        # check the user is created or print the massage
        if isinstance(self.user, ERROR_EVENT):
            print(self.user.ERROR_MASSAGE)
            exit(1)
        self.panel = None


    def tearDown(self):
        """ Cleanup the database after each test """
        self.storage.rollback()
    
    def test_user_creation(self):
        """ Test if user is correctly created """
        self.assertEqual(self.user.username, self.username)
        self.assertEqual(self.user.email, self.email)
        self.assertTrue(self.user.verify_password("1123122testpassword@Mahmoud"))
        
    def test_user_in_database(self):
        """ Test if the user is stored in the database """
        user_in_db = self.storage.getuser(self.email)
        self.assertIsNotNone(user_in_db)
        self.assertEqual(user_in_db.email, self.email)
        self.assertEqual(user_in_db.username, self.username)
    
    def test_panel_creation_using_the_constructor(self):
        """ Test if panel is correctly created """
        self.panel = Panel(name='testpanel', description='test panel description')
        self.assertIsNotNone(self.panel)
        self.assertNotIsInstance(self.panel, ERROR_EVENT)
        self.assertEqual(self.panel.name, 'testpanel')
        self.assertEqual(self.panel.description, 'test panel description')
        user_panle = UserPanel(user_id=self.user.id, panel_id=self.panel.id, access_level ='owner')
        self.assertIsNotNone(user_panle) # check the connection between the user and the panle
        self.assertNotIsInstance(user_panle, ERROR_EVENT)
        # check the data is assigned right
        self.assertEqual(user_panle.access_level, 'owner')
        self.assertEqual(user_panle.user_id, self.user.id)

    
    def test_panel_creation_using_the_create_method(self):
        """ test create method """
        self.panel = Panel.create(name='testpanel', description='test panel description')
        self.assertIsNotNone(self.panel)
        self.assertNotIsInstance(self.panel, ERROR_EVENT)
        self.assertEqual(self.panel.name, 'testpanel')
        self.assertEqual(self.panel.description, 'test panel description')
        user_panle = UserPanel.create(user_id=self.user.id, panel_id=self.panel.id, access_level ='owner')
        self.assertIsNotNone(user_panle) # check the connection between the user and the panle
        self.assertNotIsInstance(user_panle, ERROR_EVENT)
        # check the data is assigned right
        self.assertEqual(user_panle.access_level, 'owner')
        self.assertEqual(user_panle.user_id, self.user.id)
        
    def test_panel_creation_using_the_create_method_with_invalid_data(self):
        """ test create method with invalid data """
        self.panel = Panel.create(name='testpanel', description='test panel description')
        self.assertIsNotNone(self.panel)
        self.assertNotIsInstance(self.panel, ERROR_EVENT)
        self.assertEqual(self.panel.name, 'testpanel')
        self.assertEqual(self.panel.description, 'test panel description')
        user_panle = UserPanel.create(user_id=self.user.id, panel_id=self.panel.id, access_level ='invalid')
        self.assertIsInstance(user_panle, ERROR_EVENT)
        self.assertEqual(user_panle.ERROR_MASSAGE, 'Invalid access level')

    def test_panel_in_the_DB(self):
        """ Test if the panel is stored in the database """
        self.panel = Panel.create(name='testpanel', description='test panel description')
        self.assertIsNotNone(self.panel)
        self.assertNotIsInstance(self.panel, ERROR_EVENT)
        self.assertEqual(self.panel.name, 'testpanel')
        self.assertEqual(self.panel.description, 'test panel description')
        user_panle = UserPanel.create(user_id=self.user.id, panel_id=self.panel.id, access_level ='owner')
        

        self.assertIsNotNone(user_panle)
        
        panel_in_db = (self.storage.get_data('Panel', f'id={self.panel.id}')).first()
        print(" the panle ",panel_in_db)
        self.assertIsNotNone(panel_in_db)
        self.assertEqual(panel_in_db.name, 'testpanel')
        self.assertEqual(panel_in_db.description, 'test panel description')
        self.assertEqual(panel_in_db.users[0].id, self.user.id)
        
    def test_panel_deletion(self):
        """ Test if panel is correctly deleted """
        self.panel = Panel.create(name='testpanel', description='test panel description')
        self.assertIsNotNone(self.panel)
        self.assertNotIsInstance(self.panel, ERROR_EVENT)
        self.assertEqual(self.panel.name, 'testpanel')
        self.assertEqual(self.panel.description, 'test panel description')
        user_panle = UserPanel.create(user_id=self.user.id, panel_id=self.panel.id, access_level ='owner')
        self.assertIsNotNone(user_panle)
        self.assertNotIsInstance(user_panle, ERROR_EVENT)
        self.assertEqual(user_panle.access_level, 'owner')
        self.assertEqual(user_panle.user_id, self.user.id)
        
        self.storage.delete(self.panel)
        self.assertIsNone(self.storage.get_data('Panel', f'id={self.panel.id}').first())
        self.assertIsNone(self.storage.get_data('UserPanel', f'panel_id={self.panel.id}').first())
        

