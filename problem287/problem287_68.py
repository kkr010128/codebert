N = int(input())

ans = 'No'
for i in range(1,10):
    if N%i == 0:
        tmp = str(int(N/i))
        if len(tmp) >= 2:
            continue
        else:
            ans = 'Yes'
            break
    else:
        continue
print(ans)