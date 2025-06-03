n,a,b = map(int,input().split())

num1 = n%(a+b)
num2 = n//(a+b)

print(num2*a+min(num1,a))
