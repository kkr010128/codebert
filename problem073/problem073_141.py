N = int(input())
cnt = 0
for a in range(1,N):
    for b in range(1,N):
        if a * b >= N:
            break
        else:
            cnt +=1
print(cnt)
