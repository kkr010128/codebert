n=int(input())
ans="No"
for i in range(10):
    for j in range(10):
        if n==i*j:
            ans="Yes"

print(ans)