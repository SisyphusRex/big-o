"""test file"""

# System Imports
from unittest import TestCase

# First Party Imports
from alice import Alice
from bob import Bob

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
