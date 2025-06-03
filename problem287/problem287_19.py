n=int(input())

ans = False

for j in range(1,10):
    for k in range(1,10):
        if j*k == n:
            ans = True
            break
    if ans:
        break

if ans:
    print("Yes")
else:
    print("No")