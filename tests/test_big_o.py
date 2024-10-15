"""test file"""

# System Imports
from unittest import TestCase

# First Party Imports
from alice import Alice
from bob import Bob
from utility import Utility

# Third Party Imports


class TestBoth(TestCase):
    """class for testing both"""

    def setUp(self):
        self.bob = Bob()
        self.alice = Alice()

    def test_if_solutions_equal(self):
        """tests to see if both solvers have all elements"""

        # Arrange
        n: int = 5

        # Act
        self.bob.solver(n)
        self.alice.solver(n)

        # Assert
        self.assertCountEqual(self.bob.solutions, self.alice.solutions)


class TestUtility(TestCase):
    """class for testing utility module"""

    def setUp(self):
        self.utility = Utility()

    def test_for_loop_counter(self):
        """method to for loop counter test"""

        # Arrange
        def my_function():
            """function to count"""
            j = []
            yep = []
            yes = []
            for i in j:
                for k in i:
                    for yeet in yep:
                        for maybe in yes:
                            ...

        expected_count: int = 4

        # Act
        calculated_count = self.utility.count_for_loops(my_function)

        # Assert
        self.assertEqual(expected_count, calculated_count)
