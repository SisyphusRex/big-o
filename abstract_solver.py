"""problem solver super class"""

# System Imports

# First Party Imports

# Third Party imports

from abc import ABC, abstractmethod


# NOTE: The problem is
#
# Find all sets of nonnegative integers for a + b + c = n where a, b, c, n are >= 0


class AbstractSolver(ABC):
    """Interface class"""

    def __init__(self, *args, **kwargs):
        """constructor"""
        super().__init__(*args, **kwargs)
        self.count: int = 0
        self.solutions: list[tuple] = []

    @abstractmethod
    def solver(self, n: int):
        """method to solve problem"""

    def _add_solution(self, solution: tuple):
        """add solution to solution list"""
        self.solutions.append(solution)
