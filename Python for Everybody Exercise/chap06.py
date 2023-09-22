# exercise 03
def count(latter):      # create a function for latter count
    count = 0
    word = input('Write: ')
    for i in word:
        if i == 'a':    # search for 'a' in the given word
            count += 1  # increase the count value by 1 for each time found 'a'
    print(count)        # output will show how many times 'a' is there


count('abc')    # call the function

# exercise 5
str_val = 'X-DSPAM-Confidence: 0.8475'
print(str_val)
x = str_val.find(':')
y = str_val[x+1:]
print(y)
print(type(y))
z = float(y)
print('Convert in float:', z)
print(type(z))
