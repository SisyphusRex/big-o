"""main program file"""

# System Imports

# First Party Imports
from alice import Alice
from bob import Bob

# Third Party Imports


def main():
    """Method to Run program"""
    my_alice = Alice()
    my_alice.solver(10)
    print(my_alice.solutions)
    print(f"Alice iterations: {my_alice.count}")

    my_bob = Bob()
    my_bob.solver(10)
    print(my_bob.solutions)
    print(f"Bob iterations: {my_bob.count}")
