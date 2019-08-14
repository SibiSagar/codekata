# leap year or not

year=input()
year=int(year)

if year%4==0 or year%400==0:
    print("yes")

else:
    print("no")