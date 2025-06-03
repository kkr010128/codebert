import itertools

N = int(input())
S = input()

RGB = {"R":[0]*N, "G":[0]*N, "B":[0]*N}
for i in range(N):
    if S[i] == "R":
        RGB["R"][i] = 1
    elif S[i] == "G":
        RGB["G"][i] = 1
    else:
        RGB["B"][i] = 1

for k in RGB.keys():
    RGB[k] = list(itertools.accumulate(RGB[k]))

ans = 0
for i in range(N-2):
    l_i = S[i]
    for j in range(i+1, N-1):
        l_j = S[j]
        d = {"R", "G", "B"}
        if l_i != l_j:
            d.remove(l_i)
            d.remove(l_j)
            l_k = d.pop()
            ans += RGB[l_k][N-1] - RGB[l_k][j]
            if j*2 - i <= N-1:
                if S[j*2 - i] == l_k:
                    ans -= 1

print(ans)


