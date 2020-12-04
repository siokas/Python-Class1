import math

def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return int(power2(number1 - number2) / math.sqrt(power2(number1 - number2)))

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    if number1 % number2 == 0:
        return number1 / number2
    else:
        return float(number1) / number2

def power2(number):
    return number**2

