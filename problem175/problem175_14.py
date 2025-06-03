N = int(input())
S = 'X' + input()

cnt_R, cnt_G, cnt_B = 0, 0, 0
for s in S[1:]:
    if s == 'R':
        cnt_R += 1
    elif s == 'G':
        cnt_G += 1
    elif s == 'B':
        cnt_B += 1

ans = cnt_R * cnt_G * cnt_B

for i in range(1,N-1):
    for j in range(i+1,N):
        k = 2*j - i
        if k > N:
            break
        
        a = S[i]; b = S[j]; c = S[k]
        if a != b and b != c and c != a:
            ans -= 1

print(ans)