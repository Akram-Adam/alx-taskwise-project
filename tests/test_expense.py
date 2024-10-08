
import unittest
from models.expense import Expense
from models.engine.Errorevent import ERROR_EVENT
from models.panel import Panel,UserPanel
from models.user import User
from models.category import Category_expencics
import uuid
import bcrypt

 


class TestExpense(unittest.TestCase):
    
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
        """Set up test environment"""
        
        username = f"testuser_{uuid.uuid4()}"
        email = f"testuser_{uuid.uuid4()}@example.com"
        password ="1123122testpassword@Mahmoud"
        
        self.user_data = {'username' : username, 'email' : email, 'user_password' : "1123122testpassword@Mahmoud",'conformingpassword' : "1123122testpassword@Mahmoud"}

        # self.user = User.create(username=username, email=email, user_password=password, conformingpassword=password)
        self.user = User.create(**(self.user_data))
    
        if isinstance(self.user, ERROR_EVENT):
            print(self.user.ERROR_MASSAGE)
            exit(1)
        elif self.user is None:
            print("User not created")
            exit(1)

        self.panel_data = {
            'name': f'TestPanel@{uuid.uuid4()}',
            'description' : 'Test panel for testing'
        }
        self.panel = Panel.create(**(self.panel_data))
    
        if isinstance(self.panel, ERROR_EVENT):
            print(self.user.ERROR_MASSAGE)
            exit(1)
        elif self.panel is None:
            print("Panel not created")

        self.user_panel_data = {
            'panel_id': self.panel.id,
            'user_id': self.user.id,
            'access_level': 'owner'
        }
        self.user_panel = UserPanel.create(**(self.user_panel_data))
        
        if isinstance(self.user_panel, ERROR_EVENT):
            print(self.user_panel.ERROR_MASSAGE)
            exit(1)
        elif self.user_panel is None:
            print("UserPanel not created")
    
        self.category_data = {
            'name': 'Groceries',
            'description': 'Expenses related to groceries',
            'panel_id': self.panel.id
        }
        self.category = Category_expencics.create(**(self.category_data))
        
        if isinstance(self.category, ERROR_EVENT):
            print(self.category.ERROR_MASSAGE)
            exit(1)
        elif self.category is None:
            print("UserPanel not created")
    
    
        self.valid_data = {
            'title': 'Groceries',
            'description': 'Weekly grocery shopping',
            'amount': '150.75',
            'category_id': self.category.id
        }
    

    def test_create_valid_expense(self):
        """Test creating a valid expense"""
        expense = Expense.create(**self.valid_data)
        self.assertIsInstance(expense, Expense)
        self.assertEqual(expense.title, self.valid_data['title'])
        self.assertEqual(expense.description, self.valid_data['description'])
        self.assertEqual(expense.amount, float(self.valid_data['amount']))
        self.assertEqual(expense.category_id, self.valid_data['category_id'])

    def test_create_expense_missing_title(self):
        """Test creating an expense with missing title"""
        data = self.valid_data.copy()
        data['title'] = ''
        error = Expense.create(**data)
        self.assertIsInstance(error, ERROR_EVENT)
        self.assertEqual(error.ERROR_MASSAGE, " 'titel' is missing ")

    def test_create_expense_invalid_amount(self):
        """Test creating an expense with invalid amount"""
        data = self.valid_data.copy()
        data['amount'] = 'abc'
        error = Expense.create(**data)
        self.assertIsInstance(error, ERROR_EVENT)
        self.assertEqual(error.ERROR_MASSAGE, " 'amount' must be digit ")

    def test_create_expense_missing_category_id(self):
        """Test creating an expense with missing category_id"""
        data = self.valid_data.copy()
        data['category_id'] = '';                   
        error = Expense.create(**data)
        self.assertIsInstance(error, ERROR_EVENT)
        self.assertEqual(error.ERROR_MASSAGE, " 'category_id' is missing ")

    def test_delete_panel_and_related_data(self):
        """Test deleting a panel and ensuring all related data is deleted"""
        # Delete the panel
        self.panel.delete()

        # Check if the panel is deleted
        deleted_panel = self.storage.get_data('Panel', f'id={self.panel.id}')
        self.assertEqual(deleted_panel.count(), 0)

        # Check if the category is deleted
        deleted_category = self.storage.get_data('Category_expencics', f'id={self.category.id}')
        self.assertEqual(deleted_category.count(), 0)

        # Check if the expenses are deleted
        deleted_expenses = self.storage.get_data('Expense', f'category_id={self.category.id}')
        self.assertEqual(deleted_expenses.count(), 0)

        # Check if the user is not deleted
        existing_user = self.storage.get_data('User', f'id={self.user.id}')
        self.assertEqual(existing_user.count(), 1)

    def test_delete_category_and_related_expenses(self):
        """Test deleting a category and ensuring all related expenses are deleted"""
        # Delete the category
        self.category.delete()

        # Check if the category is deleted
        deleted_category = self.storage.get_data('Category_expencics', f'id={self.category.id}')
        self.assertEqual(deleted_category.count(), 0)

        # Check if the expenses are deleted
        deleted_expenses = self.storage.get_data('Expense', f'category_id={self.category.id}')
        self.assertEqual(deleted_expenses.count(), 0)

        # Check if the panel is not deleted
        existing_panel = self.storage.get_data('Panel', f'id={self.panel.id}')
        self.assertEqual(existing_panel.count(), 1)

        # Check if the user is not deleted
        existing_user = self.storage.get_data('User', f'id={self.user.id}')
        self.assertEqual(existing_user.count(), 1)

if __name__ == '__main__':
    unittest.main()
