# - Check whether a number is even or odd.

num=input()
num=int(num)

if num%2==0:
    print("Even")
elif num<0:
    print("invalid")
else:
    print("Odd")
