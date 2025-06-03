n=int(input())
l=[x for x in range (1,10)]
ans="No"
for i in range(1,10):
    if n % i == 0 and n//i in l:
        ans="Yes"
print(ans)