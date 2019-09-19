'''Simi is learning about palindromic numbers. Her teacher gave him the task to count all palindromic numbers present in that range.
Simi has told you about this and want your help. You design an algorithm in order to help simi.'''

n=input()
n=int(n)
count=0
def palin(i):
    i=str(i)
    if i==i[::-1]:
        return True
    return False
        

for i in range(0,n):
    if palin(i):
        count+=1
    
print(count)
