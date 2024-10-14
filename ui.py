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
        "(a, b, c) that sum to integer n, n >= 0"
    )

    def __init__(self):
        """constructor"""

    def display_main_menu(self) -> str:
        """displays main menu and gets input"""
        running = True
        while running:
            print(self.PROBLEM)
            print()
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
        try:
            int(input1)
        except ValueError:
            print("Must be an integer.")
            print()
            return True
        return False

    def __validate_in_main_menu(self, user_input) -> bool:
        if not self.__validate_int(user_input):
            menu_range = range(len(self.MAIN_MENU))
            user_int = int(user_input)
            if user_int in menu_range:
                return False
            return True

    def print_iteration_comparison(self, object1, object2, user_n):
        """method for printing number of iterations"""
        print(f"When n = {user_n}")
        print(object1)
        print(object2)
        print()

    def print_n_not_initiated(self):
        """print not initiated error"""
        print("Variable n not initiated yet.")
        print()
