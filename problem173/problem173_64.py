n=int(input())
result=0
for i in range(n+1):
    if (i%3)!=0 and (i%5)!=0:
        result+=i
print(result)