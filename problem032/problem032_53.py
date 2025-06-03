n = int( input() )
x = list(map(int, input().split()))
y = list(map(int, input().split()))
for i in range(1,4):
    s=0
    m=0
    for j in range(n):
        s+=(abs(x[j]-y[j]))**i
        if (abs(x[j]-y[j])) > m:
            m=(abs(x[j]-y[j]))
    print(s**(1/i))
print(m)