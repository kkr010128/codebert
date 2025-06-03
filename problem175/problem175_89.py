N = int(input())
S = input()
rgb = [0]*3

for i in range(N):
    if S[i] == "R":
        rgb[0] += 1
    elif S[i] == "G":
        rgb[1] += 1
    else:
        rgb[2] += 1
ans = 0
for i in range(N):
    for h in range(N):
        j = i+h
        k = i+2*h
        if k >= N:
            break
        if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
            ans += 1

print(rgb[0]*rgb[1]*rgb[2]-ans)
