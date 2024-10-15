"""ui module"""

# System Imports

# First Party Imports

# Third Party Imports


class UserInterface:
    """ui class"""

    MAIN_MENU: list = ["Change n", "Compare number of iterations", "Exit"]
    PROBLEM: str = (
        "a + b + c = n\n"
        "Find all sets of nonnegative integers\n"
        "(a, b, c) that sum to integer n, n >= 0\n"
    )

    def __init__(self):
        """constructor"""

    def display_problem(self) -> None:
        """method to print problem"""
        print(self.PROBLEM)

    def display_main_menu(self) -> str:
        """method to display main menu and get input"""
        running = True
        while running:
            print("Type the number of your choice:")
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
            print("For the problem a + b + c = n, give me n:")
            n = input(">")
            running = self.__validate_int(n)
            print()
        return n

    def __validate_int(self, input1) -> bool:
        """method to validate if int"""
        try:
            int(input1)
        except ValueError:
            print("Must be an integer.")
            print()
            return True
        return False

    def __validate_in_main_menu(self, user_input) -> bool:
        """method to validate if choice in menu"""
        if not self.__validate_int(user_input):
            menu_range = range(len(self.MAIN_MENU))
            user_int = int(user_input)
            if user_int in menu_range:
                return False
            return True

    def print_iteration_comparison(self, object1, object2, user_n):
        """method for printing number of iterations"""
        print(f"When n = {user_n}")
        headers = ["Name", "Iterations", "Runtime"]
        header_str = f"{headers[0]:^15}|{headers[1]:^15}|{headers[2]:^15}"
        print(header_str)
        print("-" * len(header_str))
        print(object1)
        print(object2)
        print()

    def print_n_not_initiated(self):
        """method to print not initiated error"""
        print("Variable n not initiated yet.")
        print()
