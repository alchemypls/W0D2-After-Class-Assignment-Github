import unittest
from main import greet_person, hello_world

class TestHelloWorld(unittest.TestCase):
    def test_Hello_world(self):
        self.assertEqual(hello_world(), "Hello From Richard!")
        


    def test_Greet_person(self):
        self.assertEqual(greet_person(self), f"Hello, {self}")
        

if __name__ == '__main__':
    unittest.main()