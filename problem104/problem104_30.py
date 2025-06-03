l, r, d = map(int, input().split())
result=0

for i in range(r-l+1):
    if (l+i) % d == 0:
        result+=1
print(result)
