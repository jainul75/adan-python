# exercise 03
"""
Encapsulate this code in a function named count, and generalize it so that it
accepts the string and the letter as arguments.
"""

def count(latter):      # create a function for latter count
    count = 0
    word = input('Write: ')
    for i in word:
        if i == 'a':    # search for 'a' in the given word
            count += 1  # increase the count value by 1 for each time found 'a'
    print(count)        # output will show how many times 'a' is there


count('abc')    # call the function

# exercise 5
"""
Take the following Python code that stores a string:‘
str = ’X-DSPAM-Confidence:0.8475’
Use find and string slicing to extract the portion of the string after the colon character and 
then use the float function to convert the extracted string into a floating point number.
"""
str_val = 'X-DSPAM-Confidence: 0.8475'
print(str_val)
x = str_val.find(':')
y = str_val[x+1:]
print(y)
print(type(y))
z = float(y)
print('Convert in float:', z)
print(type(z))
