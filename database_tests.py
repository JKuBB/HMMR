import unittest
import os

from database import Database

class DatabaseTests(unittest.TestCase):

    # Test case setup, runs before each test method is executed
    def setUp(self):
        self.db = Database("test.db")
    
    # Test case teardown, runs after each test method execution
    def tearDown(self):
        os.remove("test.db")

    # Tests that we can create a user, and that the user is defined after creation
    def test_create_user_does_create_user(self):
        self.db.create_user("foo", 1, "bar")

        user = self.db.get_user("foo")

        self.assertIsNotNone(user)
    
    # Tests that correct data is returned when user is selected
    def test_get_user_returns_correct_data(self):
        self.db.create_user("foo", 650, "bar")

        user = self.db.get_user("foo")

        self.assertEqual(1, user[0])        # 0 = UserId
        self.assertEqual("foo", user[1])    # 1 = Username
        self.assertEqual(650, user[2])      # 2 = MMR
        self.assertEqual(0, user[3])        # 3 = Wins
        self.assertEqual(0, user[4])        # 4 = Losses
        self.assertEqual(0, user[5])        # 5 = Draws
        self.assertEqual(0, user[6])        # 6 = Games
        self.assertEqual("bar", user[7])    # 7 = Rank
        
    def test_create_user_does_not_allow_duplicate_names(self):
        try:
            self.db.create_user("foo", 1, "bar")
            self.db.create_user("foo", 1, "bar")

            self.assertFalse(1 == 1, "We should not have been allowed to create duplicate usernames")
        except Exception:
            # expected
            pass

    # should increment win by exactly 1. Default is 0
    def test_increment_user_win_functions_appropriately(self):
        self.db.create_user("foo", 1, "bar")
        self.db.increment_user_win("foo")

        user = self.db.get_user("foo")

        self.assertEqual(1, user[3])

    # should increment loss by exactly 1. Default is 0
    def test_increment_user_loss_functions_appropriately(self):
        self.db.create_user("foo", 1, "bar")
        self.db.increment_user_loss("foo")

        user = self.db.get_user("foo")

        self.assertEqual(1, user[4])

    # should increment draw by exactly 1. Default is 0
    def test_increment_user_draw_functions_appropriately(self):
        self.db.create_user("foo", 1, "bar")
        self.db.increment_user_draw("foo")

        user = self.db.get_user("foo")

        self.assertEqual(1, user[5])

    # should increment game by exactly 1. Default is 0
    def test_increment_user_game_functions_appropriately(self):
        self.db.create_user("foo", 1, "bar")
        self.db.increment_user_game("foo")

        user = self.db.get_user("foo")

        self.assertEqual(1, user[6])

    # should increment mmr by exactly 1. Default is 0
    def test_increment_user_mmr_functions_appropriately(self):
        self.db.create_user("foo", 620, "bar")
        self.db.increment_user_mmr("foo", 30)

        user = self.db.get_user("foo")

        self.assertEqual(650, user[2])

        # make sure this works for decrementing, as well.
        self.db.increment_user_mmr("foo", -40)
        user = self.db.get_user("foo")

        self.assertEqual(610, user[2])

    def test_set_user_rank_functions_appropriately(self):
        self.db.create_user("foo", 620, "yeet")
        
        user = self.db.get_user("foo")

        self.assertEqual("yeet", user[7])

        self.db.set_user_rank("foo", "yoink")

        user = self.db.get_user("foo")

        self.assertEqual("yoink", user[7])

    def test_delete_user_removes_user_from_table(self):
        self.db.create_user("foo", 620, "yeet")

        user = self.db.get_user("foo")

        self.assertIsNotNone(user)

        self.db.delete_user("foo")

        user = self.db.get_user("foo")

        self.assertIsNone(user)

    def test_get_all_users(self):
        self.db.create_user("mynameismawky", -1, "ultramegasupertrash")
        self.db.create_user("JKuBB_", 650, "A Solid Plat")
        self.db.create_user("MisterJW", 9000, "Grand Bronze")
        
        users = self.db.get_all_users()

        self.assertEqual(3, len(users))


    
if __name__ == '__main__':
    unittest.main()