a,b,c,d = map(int,input().split())

result = max(max(a*c,a*d),max(b*c,b*d))
    
print(result)