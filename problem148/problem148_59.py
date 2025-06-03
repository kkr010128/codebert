a,b,c,k = map(int,input().split())

print(k if k<a else a if a+b>k else a-(k-a-b))
