# exercise 06
def computepay(hours, rates):
    print('in computepay', 'H:', hour, 'R:', rate)


hour = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
computepay(hour, rate)
if hour > 40:
    over_pay = (hour*rate) + ((hour-40) * (rate*.5))
    print('Pay:', over_pay)
else:
    reg_pay = hour * rate
    print('Pay:', reg_pay)

# exercise 07
def computegrade(scores):
    print('Mark:', scores)
try:
    score = float(input('Enter your grade: '))
    computegrade(score)
    if score > 1:
        print('Bad score')
    elif score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    elif score < 0.6:
        print('F')
except:
    print('Bad score!!!')