#prime or not

def isprime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

num=input()
num=int(num)

if isprime(num):
    print("yes")
else:
    print("no")