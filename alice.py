"""Alice Solution module"""

# System Imports

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

    def solver(self, n: int):
        """Alice method to solve"""
        for a in range(n + 1):
            for b in range(n + 1):
                self.count += 1
                c = n - (a + b)
                if c >= 0:
                    self._add_solution((a, b, c))
