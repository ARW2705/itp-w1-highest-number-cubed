"""This is the entry point of the program."""


def highest_number_cubed(limit):
    test = 1
    while True:
        if test ** 3 <= limit:
            test += 1
        else:
            return (test - 1)  
