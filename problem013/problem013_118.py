'''
Rjの最小値を保持することで最大利益の更新判定をn回で終わらせる
'''

r = []

n = int(input())
for i in range(n):
    i = int(input())
    r.append(i)

minv = r[0]
maxv = r[1] - r[0]

for j in range(1,n):
    maxv = max(maxv, r[j]-minv)
    minv = min(minv, r[j])

print(maxv)

