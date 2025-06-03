from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

#%%
d = defaultdict(lambda: 0)
for key in A:
    d[key] += 1

#%%
# それぞれのkeyのnC2
cmb = dict()
cmb2 = dict()
for k in d.keys():
    cmb[k] = d[k] * (d[k] - 1) // 2
    cmb2[k] = (d[k] - 1) * (d[k] - 2) // 2

#%%
ans_d = dict()
s = sum(cmb.values())
for k in d.keys():
    ans_d[k] = s - cmb[k] + cmb2[k]
#%%
for a in A:
    print(ans_d[a])
