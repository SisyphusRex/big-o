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

    def solver(self, n: int):
        """bobs method to solve"""
        super().solver()
        timer_start = perf_counter()
        for a in range(n + 1):
            for b in range(n + 1):
                for c in range(n + 1):
                    self.count += 1
                    if n == a + b + c:
                        self._add_solution((a, b, c))
        timer_stop = perf_counter()
        self.timer = timer_stop - timer_start

    @property
    def _name(self):
        return "Bob"
