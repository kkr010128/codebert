S = list(input())
count = 0
ans = 0

for i in range(len(S)):
    if S[i] == 'R':
        count += 1
        if ans < count:
            ans = count
    else:
        count = 0

    
print(ans)