import unittest
from main import hello_world

class TestHelloWorld(unittest.TestCase):
    def test_Hello_world(self):
        self.assertEqual(hello_world(), "Hello from Richard!")

if __name__ == '__mina__':
    unittest.main()