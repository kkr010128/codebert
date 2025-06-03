n=int(input())
t_won=0
h_won=0
for _ in range(n):
    t_wd,h_wd = input().split()
    if   t_wd > h_wd: t_won += 1
    elif t_wd < h_wd: h_won += 1
print(t_won*3 + (n-t_won-h_won), h_won*3 + (n-t_won-h_won))