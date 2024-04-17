import unittest

from src.creational.singleton.singleton import Singleton


class TestSingleton(unittest.TestCase):

    def test_single_instance_creation(self):
        """
        Test if the Singleton class returns the same instance when called
        multiple times.

        This test function creates two instances of the Singleton class and
        asserts that they are the same object.

        Parameters:
            self (TestSingleton): The test case instance.

        Returns:
            None
        """
        obj1 = Singleton()
        obj2 = Singleton()
        self.assertIs(obj1, obj2, "Instances are not the same")

    def test_same_instance_returned(self):
        """
        A test function to check if the same instance is returned by the
        Singleton class.
        """
        obj1 = Singleton()
        obj2 = Singleton()
        self.assertEqual(id(obj1), id(obj2), "Instances are different")


if __name__ == '__main__':
    unittest.main()
