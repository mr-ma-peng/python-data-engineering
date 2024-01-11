"""
This model is used to test static code analyze
"""


def add(number1, number2):
    """
     This function is the addition of two numbers
    """
    return number1 + number2


NUM_1 = 4
NUM_2 = 5
TOTAL = add(NUM_1, NUM_2)
print(f"The sum of {NUM_1} and {NUM_2} is {TOTAL}")
