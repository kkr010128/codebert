n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
d= [abs(x[i] - y[i]) for i in range(n)]
for i in range(1, 4):
    a = 0
    for j in d:
        a += j**i
    print("{:.6f}".format(a**(1/i)))
print("{:.6f}".format(max(d)))
