# Exercise 01
hour = input('Enter hours: ')
rate = input('Enter rate: ')  # regular rate=10 and overtime rate=1.5
if float(hour) > 40:
    c = float(hour) * float(rate)   # pay in regular rate that is 10
    d = (float(hour)-40) * (float(rate)*.5)  # i already pay 10$ and the overtime rate is (10*1.5)=15,so i have to pay just 5$ (10*.5)=5
    e = float(c) + float(d)
    print('Pay:', e)
else:
    f = float(hour) * float(rate)    # pay in regular rate that is 10
    print('Pay:', f)

print('Payment Done!')

# Exercise 02
try:
    hour = input('Enter hours: ')
    rate = input('Enter rate: ')
    if float(hour) > 40:
        c = float(hour) * float(rate)
        d = (float(hour)-40) * (float(rate)*.5)
        e = float(c) + float(d)
        print('Pay:', e)
    else:
        f = float(hour) * float(rate)
        print('Pay:', f)
except:
    print('Error, please enter numeric input.')

# Exercise 03
try:
    score = input('Enter score: ')
    if float(score) > 1:
        print('Bad Score')
    elif float(score) >= 0.9:
        print('A')
    elif float(score) >= 0.8:
        print('B')
    elif float(score) >= 0.7:
        print('C')
    elif float(score) >= 0.6:
        print('D')
    elif float(score) < 0.6:
        print('F')
except:
    print('Bad score')

print('Chap03 complete')
print('Well Done!!!')
