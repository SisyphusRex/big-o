# Copyright 2025 Theodore Podewil
# GPL-3.0-or-later

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 


"""problem solver super class"""

# System Imports
from time import perf_counter

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

    def solver(self, n: int):
        """abstract method to solve problem"""
        self.count = 0
        self.solutions.clear()
        self.timer = 0.00
        timer_start = perf_counter()
        self._child_solver(n)
        timer_stop = perf_counter()
        self.timer = timer_stop - timer_start

    @abstractmethod
    def _child_solver(self, n: int):
        """abastr"""
        # this is necessary for reference in the solver method in between the timers

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
