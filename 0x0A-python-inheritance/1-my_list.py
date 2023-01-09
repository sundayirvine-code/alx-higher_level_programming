#!/usr/bin/python3
class MyList(list):
    """
    A class that inherits from list and has a method to print the list in ascending order.
    """

    def print_sorted(self):
        """
        Print the list in ascending order.
        """
        print(sorted(self))
