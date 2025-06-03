N,A,B = map(int,input().split())

x = N //(A+B)
y = min(N%(A+B),A)
print(x * A + y)