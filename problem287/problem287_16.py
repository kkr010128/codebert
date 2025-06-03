n=int(input())
ans="No"
for i in range(1,10):
    for j in range(1,10):
        if n==i*j:
            ans="Yes"
            break
    else:
        continue
    break
print(ans)