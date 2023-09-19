# To know height in metres
# print("If you don't know your height in metres, it's OK")
# print('Use this!!!')
a = float(input('Enter your height(foot): '))
b = float(input('Enter your height(inch): '))
height_metre = (a * 0.3048) + (b * 0.0254)
print('Your height in metres: ', height_metre)

name = input('Enter your name: ')
weight = float(input('Enter your weight(in kg): '))
height = float(height_metre)
bmi = weight / (height ** 2)
print('Hello', name)
print('Your BMI is: ', bmi)
if bmi < 18.5:
    print('You are in Underweight!!!')
elif bmi >= 18.5 and bmi <= 24.9:
    print(name, 'You are Healthy')
elif bmi >= 25.0 and bmi <= 29.9:
    print(name, 'You gain Overweight?')
else:
    print('Obese')
print('Be healthy!')
