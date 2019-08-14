# Given 2 numbers  N,K  and an array of N intgers, find the sum  of the "K" integers

N,K=input().split()
N=int(N)
K=int(K)
N_arr=[int(i) for i in input().split()]

print(sum(N_arr[:K]))