#print the prime numbers which lies b/w the range


def isprime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

N,Q=input().split()
N=int(N)
Q=int(Q)

for i in range(N+1,Q):
    if isprime(i):
        print(i,end=" ")