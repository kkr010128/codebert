from sys import stdin
n = int(input())
r=[int(input()) for i in range(n)]
rv = r[::-1][:-1]
m = None
p_r_j = None
for j,r_j in enumerate(rv):
    if p_r_j == None or p_r_j < r_j:
        p_r_j = r_j
    if p_r_j > r_j:
        continue
    r_i = min(r[:-(j+1)])
    t = r_j - r_i
    if m == None or t > m:
        m = t
print(m)