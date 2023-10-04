# Exercise02
"""
Write a program that uses input to prompt a user for their name and then welcomes them.
"""
name = input('Enter your name: ')
print('Hello', name)

# Exercise03
"""
Write a program to prompt the user for hours and rate per hour to compute gross pay.
Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25
"""
a = input('Enter Hours: ')
b = input('Enter Rate: ')
c = float(a)*float(b)
print('Pay:', c)

# Exercise04
"""
Assume that we execute the following assignment statements:
width = 17
height = 12.0
For each of the following expressions, write the value of the expression and the type (of the value of the expression).
1. width//2
2. width/2.0
3. height/3
4. 1 + 2 \* 5
"""

width = 17
height = 12.0
v1 =width//2
v2 = width/2.0
v3 = height/3
print(v1)
print(v2)
print(v3)
type(v1)
type(v2)
type(v3)

# Exercise05
"""
Write a program which prompts the user for a Celsius temperature, convert 
the temperature to Fahrenheit, and print out the converted temperature.
"""
# Celsius to Fahrenheit
temp = input('Celsius: ')
Fahrenheit = ((9/5)*float(temp))+32
print('Temperature in fahrenheit is:', Fahrenheit)
# Fahrenheit to Celsius
temp = input('Fahrenheit: ')
Celsius = ((5/9)*(float(temp)-32))
print('Temperature in celsius is:', Celsius)
