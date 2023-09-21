# exercise 5.1
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
