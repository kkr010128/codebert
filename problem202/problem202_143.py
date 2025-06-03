n,a,b = map(int,input().split())
answer = 0
answer = a*(n//(a+b))
n = n%(a+b)
answer += min(a,n)
print(answer)