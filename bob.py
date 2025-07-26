# Copyright 2025 Theodore Podewil
# GPL-3.0-or-later

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 


"""bob solver module"""

# System Imports
from time import perf_counter

# First Party Imports
from abstract_solver import AbstractSolver

# Third Party Imports


class Bob(AbstractSolver):
    """bob's solver class"""

    def __init__(self):
        """constructor"""
        super().__init__()

    def __str__(self):
        """string method"""
        return f"{super().__str__()}"

    def _child_solver(self, n: int):
        """bobs method to solve"""
        for a in range(n + 1):
            for b in range(n + 1):
                for c in range(n + 1):
                    self.count += 1
                    if n == a + b + c:
                        self._add_solution((a, b, c))

    @property
    def _name(self):
        return "Bob"
