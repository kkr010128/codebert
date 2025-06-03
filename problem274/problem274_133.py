n, m = map(int, input().split())
S = input()

ans = []
x = len(S) - 1
while x:
    for step in range(m, 0, -1):
        if x - step < 0:
            continue
            
        to = S[x-step]
        if to == '1':
            continue
        else:
            x -= step
            ans.append(str(step))
            break
    else:
        print(-1)
        exit()

print(' '.join(ans[::-1]))