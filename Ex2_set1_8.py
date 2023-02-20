year=int(input('Enter the year: '))

if year % 4==0:
    if year % 100==0:
        if year % 400==0:
            print("It is a leap year:",year)
        else:
            print("It is not a leap year:",year)
    else:
        print("Is leap year: ",year)
else:
     print("Is not leap year: ",year)
