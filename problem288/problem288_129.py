N = int(input())
a = 0
for i in range(1,int(N**0.5)+1):
    if N%i == 0:
        a = max(a,i)
b = N//a
print((a-1)+(b-1))