""" 
testing module for user
create
delete
update

"""


import unittest
from models.user import User
from models.engine.dp_manager import DBStorage
from models.engine.Errorevent import ERROR_EVENT
import uuid
import bcrypt
from sqlalchemy.exc import IntegrityError

class TestUser(unittest.TestCase):
    """ Test cases for User class """

    @classmethod
    def setUpClass(cls):
        """ Set up for the tests. Initialize DBStorage """
        #cls.storage = DBStorage()
        #cls.storage.reload()  # Reload database/tables
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
        self.user = User(username=self.username, email=self.email, user_password="password123")

    def tearDown(self):
        """ Cleanup the database after each test """
        self.storage.rollback()  # Rollback any changes made during the test

    def test_user_creation(self):
        """ Test if user is correctly created """
        self.assertEqual(self.user.username, self.username)
        self.assertEqual(self.user.email, self.email)
        self.assertTrue(self.user.verify_password("password123"))

    def test_user_in_database(self):
        """ Test if the user is stored in the database """
        user_in_db = self.storage.getuser(self.email)
        self.assertIsNotNone(user_in_db)
        self.assertEqual(user_in_db.email, self.email)

    def test_user_duplicate(self):
        """ Test if duplicate users are not allowed """
        # Create a user with the same email and username
        with self.assertRaises(IntegrityError):
            duplicate_user = User(username=self.username, email=self.email, user_password="password123")
        

    def test_user_deletion(self):
        """ Test if user can be deleted """
        self.storage.delete(self.user)
        user_in_db = self.storage.getuser(self.email)
        self.assertIsNone(user_in_db)


    def test_user_create(self):
        """ Test create function test the user in the database """
        object_username =  f"testuser_{uuid.uuid4()}"
        object_email =  f"testuser_{uuid.uuid4()}@example.com"
        object_password =  "1123122testpassword@Mahmoud"
        object_ = User.create(username=object_username, email=object_email, user_password=object_password, conformingpassword=object_password)
        self.assertIsNotNone(object_)
        object_from_database = self.storage.getuser(usernameoremail=object_email)
        self.assertIsNotNone(object_from_database)
        if isinstance(object_, ERROR_EVENT):
            print(object_)
        print(object_)
        self.assertEqual(object_.id, object_from_database.id)
        self.assertEqual(object_.user_password, object_from_database.user_password)
        self.assertEqual(object_.verify_password(object_password), True)
        user_test_log_in = User.log_in_check(username_or_email=object_email, password=object_password) # shluld return instance
        self.assertIsNotNone(user_test_log_in)
        self.assertIsInstance(user_test_log_in, User)
        self.assertEqual(user_test_log_in.id, object_.id)

if __name__ == "__main__":
    unittest.main()
