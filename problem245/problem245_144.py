#https://atcoder.jp/contests/abc150/tasks/abc150_b
N= int(input())
s= input()

A= []
A= list(s)

#print(A)

add = 0
for i in range(0, N-2):
    if A[i]== 'A' and A[i+1]=='B' and A[i+2]=='C':
        add = add + 1

print(add)