# a year is a leap year if it is divisible by 4 but not divisible by 100 unless it is also divisible by 400
# leap year determination

# version 1
year=int(input('enter the year: '))

if year%4==0 and year%100 !=0:
    print('leap year')
elif year%100==0 and year%400==0:
    print('leap year')
else:
    print('not a leap year')

# version 2
year=int(input('enter the year: '))

if year%400==0:
    print('leap year')
elif year%100==0:
    print('not a leap year')
elif year%4==0:
    print('leap year')
else:
    print('not a leap year')

# version 3
year=int(input('enter the year: '))

if year%4 !=0:
    print('not a leap year')
else:
    if year%100==0:
        if year%400==0:
            print('leap year')
        else:
            print('not a leap year')
    else:
        print('leap year')
