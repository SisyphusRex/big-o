"""bob solver module"""

# System Imports

# First Party Imports
from abstract_solver import AbstractSolver

# Third Party Imports


class Bob(AbstractSolver):
    """bob's solver class"""

    def __init__(self):
        """constructor"""
        super().__init__()

    def solver(self, n: int):
        for a in range(n + 1):
            for b in range(n + 1):
                for c in range(n + 1):
                    self.count += 1
                    if n == a + b + c:
                        self._add_solution((a, b, c))
