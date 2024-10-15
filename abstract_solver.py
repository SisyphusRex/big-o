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
        self.timer: float = 0.00

    def __str__(self):
        """string method"""
        return f"{self._name:^15}|{self.__format_count:>15}|{self.__format_time:^15}"

    @abstractmethod
    def solver(self):
        """abstract method to solve problem"""
        self.count = 0
        self.solutions.clear()
        self.timer = 0.00

    @property
    @abstractmethod
    def _name(self):
        """method for name of class"""

    def _add_solution(self, solution: tuple):
        """add solution to solution list"""
        self.solutions.append(solution)

    @property
    def __format_time(self) -> str:
        """format time to 5 decimal places"""
        return f"{self.timer:.5f} s"

    @property
    def __format_count(self) -> str:
        """format count to have commas"""
        return f"{self.count:,}"
