"""Alice Solution module"""

# System Imports
from time import perf_counter

# First Party Imports
from abstract_solver import AbstractSolver

# Third Party Imports

# Alice's solution is:
#   For all (a, b), c = n - (a + b)
#   if c >= 0
#       print (a, b, c)


class Alice(AbstractSolver):
    """Alice solution class"""

    def __init__(self):
        """constructor"""
        super().__init__()

    def __str__(self):
        """string method"""
        return f"{super().__str__()}"

    def solver(self, n: int):
        """Alice method to solve"""
        super().solver()
        timer_start = perf_counter()
        for a in range(n + 1):
            for b in range(n + 1):
                self.count += 1
                c = n - (a + b)
                if c >= 0:
                    self._add_solution((a, b, c))
        timer_stop = perf_counter()
        self.timer = timer_stop - timer_start

    @property
    def _name(self):
        return "Alice"
