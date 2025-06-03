n,a,b= map(int,input().split())

loop = n//(a+b)
r = n%(a+b)

before_count  = loop * a
after_count = min(r,a)
ans = before_count + after_count

print(ans)