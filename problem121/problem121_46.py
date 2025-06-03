from itertools import accumulate
a=[]
for i in range(12):
    a.append(26**i)
b=list(accumulate(a))

alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

N=int(input())

num=0
for i in range(12):
    if N < b[i] :
        num=i
        break

M=N-b[num-1]
r=M
for i in range(num):
    q=r//26**(num-i-1)
    r=r%26**(num-i-1)
    print(alpha[q],end='')