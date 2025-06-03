N, M = map(int, input().split())
pSs = [list(map(str, input().split())) for _ in range(M)]

#%%

ACs = [False for _ in range(N)]
WAs = [0 for _ in range(N)]

for pS in pSs:
    problem = int(pS[0]) -1
    answer = pS[1]
    if ACs[problem] == True:
        continue
    else:
        if answer == "WA":
            WAs[problem] += 1
        else:
            ACs[problem] = True

num_WA = 0
for i, WA in enumerate(WAs):
    if ACs[i] == True:
        num_WA += WA

print(sum(ACs), num_WA)