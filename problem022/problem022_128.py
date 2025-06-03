n=int(input())
S=[int(i) for i in input().split()]
q=int(input())
T=[int(i) for i in input().split()]
s=0
for i in range(q):
    if T[i] in S:
        s+=1
print(s)
