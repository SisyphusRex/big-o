"""module for utilities"""

# System Imports
import inspect

# First Party Imports

# Third Party Imports


class Utility:
    """Utility class"""

    def count_for_loops(self, solver_method: object) -> int:
        """method for counting for loops in function"""
        counter: int = 0
        function_string: str = self.__convert_function_to_string(solver_method)
        my_list: list = function_string.split()
        for item in my_list:
            if item == "for":
                counter += 1
        return counter

    def __convert_function_to_string(self, function: object) -> str:
        """converts function to string"""
        function_string: str = inspect.getsource(function)
        return function_string
