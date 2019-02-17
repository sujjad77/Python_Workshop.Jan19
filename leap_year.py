_year=input("enter a year:")
year=int(_year)
if(year%4==0 and year%100==0 and year%400==0):
    print("{} is a leap year".format(year))
else:
    print("{} isnot a leap year".format(year))
