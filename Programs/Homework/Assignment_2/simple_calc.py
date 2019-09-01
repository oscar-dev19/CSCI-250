"""
A simple calculator application.
Author: Oscar Lopez
"""

"""Simple Math functions."""

# Simple addition function that adds two integers and returns addition output.
def add_int(num1, num2):
    return num1 + num2


# Simple subtract function that subtracts two integers and returns substraction
# output.
def subtract_int(num1, num2):
    return num1 - num2


# Simple division function that divides two integers and returns division
# output.
def divide_int(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("ERROR: Division by zero!")
        return None


# Simple multiplication function that multiplies two integers and returns
# multiplication output.
def multiply_int(num1, num2):
    return num1 * num2


# Simple power multiplication function that takes the base and returns its
# exponential power.
def power_int(base, power):
    return base **power


# Simple modulus function that takes two integers and returns its modulus
# output.
def modulo_int(num1, num2):
    return num1%num2


""" Prompt functions / User input functions. """

def intro_prompt():
    print('''Simple Calculator
            ====================
            Options
            1. Add
            2. Subtract
            3. Multiply
            4. Divide
            5. Power
            6. Modulo
            7. Exit
            ====================''')


def input_choice(choice, num1, num2):
    if choice < 1 or choice > 7:
        print("Wrong option!")
        return None
    if choice == 1:
        return add_int(num1, num2)
    if choice == 2:
        return subtract_int(num1, num2)
    if choice == 3:
        return multiply_int(num1, num2)
    if choice == 4:
        return divide_int(num1, num2)
    if choice == 5:
        return power_int(num1, num2)
    if choice == 6:
        return modulo_int(num1, num2)
    print('Exiting Program.')
    exit()

def prompt_choice():
    intro_prompt()
    choice = input('Enter choice from menu: ')
    return choice


""" Main program """
while True:
    try:
        first_num = int(input('Enter first number: '))
        second_num = int(input('Enter second number: '))
    except:
        print('ERROR: Please enter a valid number to calculate.')
        continue
    try:
        user_choice = int(prompt_choice())
    except:
        print('ERROR: Please enter a valid numerical choice.')
        continue
    answer = input_choice(user_choice, first_num, second_num)
    if answer is not None:
        print("The answer is\n%d"%answer)
        break
