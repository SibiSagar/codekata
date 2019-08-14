#print the even numbers which lies b/w the range

N,Q=input().split()
N=int(N)
Q=int(Q)

for i in range(N+1,Q):
    if i%2==0:
        print(i,end=" ")