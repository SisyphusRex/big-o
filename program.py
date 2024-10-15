"""main program file"""

# System Imports
import sys

# First Party Imports
from alice import Alice
from bob import Bob
from ui import UserInterface
from utility import Utility

# Third Party Imports


def main():
    """Method to Run program"""

    # initialization
    my_ui = UserInterface()
    my_bob = Bob()
    my_alice = Alice()
    my_utility = Utility()
    user_n: int = -1
    running: bool = True

    # display main problem
    my_ui.display_problem()

    # this is the main decision tree based on menu choices
    while running:
        choice: str = my_ui.display_main_menu()
        match int(choice):
            case 0:
                # changes n value
                user_n: int = int(my_ui.get_n())
            case 1:
                # runs solvers and displays statistics
                if user_n >= 0:
                    my_bob.solver(user_n)
                    bob_for_loops: int = my_utility.count_for_loops(my_bob.solver)
                    my_alice.solver(user_n)
                    alice_for_loops: int = my_utility.count_for_loops(my_alice.solver)
                    my_ui.print_iteration_comparison(
                        my_bob, bob_for_loops, my_alice, alice_for_loops, user_n
                    )
                else:
                    my_ui.print_n_not_initiated()
            case 2:
                # exits
                sys.exit()
