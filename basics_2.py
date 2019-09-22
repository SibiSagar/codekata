'''
Find the minimum among 10 numbers.
Sample Testcase :
INPUT
5 4 3 2 1 7 6 10 8 9
OUTPUT
1
'''

num_list=map(int,input().split())
num_list=sorted(num_list)
print(num_list[0])
