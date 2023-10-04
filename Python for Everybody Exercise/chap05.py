# exercise 5.1
"""
Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the
numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
"""
# initialize the variables with 0 value
count = 0
total = 0
while True:
    num = input('Enter a number: ')     # take user input
    if num == 'done':   # if the user wants to exit the loop write 'done'
        break
    try:
        float_num = float(num)  # convert the user input to float
    except ValueError:
        print('Invalid')
        continue
    count += 1      # for each new valid input count will increase by 1
    total += float_num  # input number will be added with total value

print('Count:', count)
print('Total', total)

average = total / count
print('avg:', average)

# exercise 5.2
"""
Write another program that prompts for a list of numbers as above and at the end 
prints out both the maximum and minimum of the numbers instead of the average.
"""
max_val = None
min_val = None
while True:
    try:
        value = input("Enter a number: ")     # take user input
        if value == "done":     # if the user wants to exit the loop write 'done'
            break
        num = int(value)    # convert the user input to an integer
        if max_val is None or num > max_val:
            max_val = num
        elif min_val is None or num < min_val:
            min_val = num
    except ValueError:
        print("Invalid input")

print("Maximum value:", max_val)
print("Minimum value:", min_val)
