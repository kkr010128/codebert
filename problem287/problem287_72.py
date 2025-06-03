N = int(input())

ans = "No"
for s in range(1, 10):
    if N % s != 0:
        continue
    else:
        if int(N/s) <= 9:
            ans = "Yes"
            break
            
print(ans)