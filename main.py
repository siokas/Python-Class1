from calculator import *
from ColorSensor import *

x = input("Type first number: ")
x = int(x)

y = input("Type second number: ")
y = int(y)

print(addition(x,y))
print(subtraction(x,y))
print(multiplication(x,y))
print(division(x,y))

color = Color()
color.addition(1,4)
