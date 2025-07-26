# Copyright 2025 Theodore Podewil
# GPL-3.0-or-later

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 


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
