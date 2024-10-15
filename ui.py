"""ui module"""

# System Imports

# First Party Imports
from colors import print_blue, print_green, print_red, print_yellow

# Third Party Imports


class UserInterface:
    """ui class"""

    MAIN_MENU: list = ["Change n", "Compare algorithm efficiency", "Exit"]
    PROBLEM: str = (
        "a + b + c = n\n"
        "Find all sets of nonnegative integers\n"
        "(a, b, c) that sum to integer n, n >= 0\n"
    )

    def __init__(self):
        """constructor"""

    def display_problem(self) -> None:
        """method to print problem"""
        print_blue(self.PROBLEM)

    def display_main_menu(self) -> str:
        """method to display main menu and get input"""
        running: bool = True
        while running:
            print_green("Type the number of your choice:")
            for index, value in enumerate(self.MAIN_MENU):
                print(index, value)
            user_input: str = input(">")
            running = self.__validate_in_main_menu(user_input)
            print()
        return user_input

    def get_n(self) -> str:
        """method to get n"""
        running: bool = True
        while running:
            print_green("For the problem a + b + c = n, give me n:")
            n = input(">")
            running = self.__validate_int(n)
            print()
        return n

    def __validate_int(self, input1) -> bool:
        """method to validate if int"""
        try:
            int(input1)
        except ValueError:
            print()
            print_red("Must be an integer.")
            return True
        return False

    def __validate_in_main_menu(self, user_input) -> bool:
        """method to validate if choice in menu"""
        if not self.__validate_int(user_input):
            menu_range: range = range(len(self.MAIN_MENU))
            user_int = int(user_input)
            if user_int in menu_range:
                return False
            print()
            print_red("Not a valid choice.")
            return True
        return True

    def print_iteration_comparison(
        self, object1: object, object2: object, user_n
    ) -> None:
        """method for printing number of iterations"""
        print(f"When n = {user_n}")
        headers: list[str] = ["Name", "Iterations", "Runtime"]
        header_str: str = f"{headers[0]:^15}|{headers[1]:^15}|{headers[2]:^15}"
        print(header_str)
        print("-" * len(header_str))
        print(object1)
        print(object2)
        print()

    def print_n_not_initiated(self) -> None:
        """method to print not initiated error"""
        print_yellow("Variable n not initiated yet.")
        print()
