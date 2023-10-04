# exercise 01
"""
Write a program to read through a file and print the contents of the
file (line by line) all in upper case.
"""

print('Exercise 01')
f_open = open('adan05.txt')     # open a file named adan05.txt
read_file = f_open.read()
cap_file = read_file.upper()    # convert all text into upper case
print(cap_file)

# exercise 02

"""
Write a program to prompt for a file name, and then read through the file and look for lines of the form:
X-DSPAM-Confidence:0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number 
on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach 
the end of the file, print out the average spam confidence.

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745
Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519
"""
print('Exercise 02')
file_name = input('Enter the file name: ')  # enter the file name that you want to open
file = open(file_name)
count = 0
total = 0
for line in file:
    if not line.startswith('X-DSPAM-Confidence:'): continue
    count += 1
    x = line.find(':')
    y = line[x+1:]
    total = total + float(y)
avg = total/count
print('Average spam confidence:', avg)

# exercise 03
"""
Sometimes when programmers get bored or want to have a bit of fun,
they add a harmless Easter Egg to their program Modify the program that prompts
the user for the file name so that it prints a funny message when the user types in
the exact file name “na na boo boo”. The program should behave normally for all
other files which exist and don’t exist. Here is a sample execution of the program:

python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt
python egg.py
Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt
python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!
"""
print('Exercise 03')
file_name = input('Enter the file name: ')
try:
    file = open(file_name)
except FileNotFoundError:
    if file_name == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        print('File cannot be opened:', file_name)
    quit()
count = 0
for i in file:
    i = i.rstrip()
    if i.startswith('Subject:'):
        count += 1
print(count)



