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
        running = True
        while running:
            print_green("Type the number of your choice:")
            for index, value in enumerate(self.MAIN_MENU):
                print(index, value)
            user_input = input(">")
            running = self.__validate_in_main_menu(user_input)
            print()
        return user_input

    def get_n(self) -> str:
        """method to get n"""
        running = True
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
            menu_range = range(len(self.MAIN_MENU))
            user_int = int(user_input)
            if user_int in menu_range:
                return False
            print()
            print_red("Not a valid choice.")
            return True
        return True

    def print_iteration_comparison(
        self, object1, for_loops1: int, object2, for_loops2: int, user_n
    ):
        """method for printing number of iterations"""
        print(f"When n = {user_n}")
        headers = ["Name", "Iterations", "Runtime", "Big O"]
        header_str = (
            f"{headers[0]:^15}|{headers[1]:^15}|{headers[2]:^15}|{headers[3]:^15}"
        )
        object1_big_o: str = f"n^{for_loops1}"
        object2_big_o: str = f"n^{for_loops2}"
        print(header_str)
        print("-" * len(header_str))
        print(f"{object1}|{object1_big_o:^15}")
        print(f"{object2}|{object2_big_o:^15}")
        print()

    def print_n_not_initiated(self):
        """method to print not initiated error"""
        print_yellow("Variable n not initiated yet.")
        print()
