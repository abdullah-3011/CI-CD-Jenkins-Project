import unittest
from app import welcome, add_numbers

class TestApplication(unittest.TestCase):

    def test_welcome(self):
        self.assertEqual(
            welcome(),
            "Welcome to CI/CD Pipeline Automation using Jenkins and GitHub!"
        )

    def test_addition(self):
        self.assertEqual(add_numbers(10, 20), 30)

    def test_addition_zero(self):
        self.assertEqual(add_numbers(5, 0), 5)

if __name__ == "__main__":
    unittest.main()
    