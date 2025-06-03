a,b,c = map(int,input().split())
if 4*a*b < (c-a-b)**2 and c-a-b > 0:
    ans = 1
else:
    ans = 0
print(["No","Yes"][ans])