# L = x + y + z
# S = x*y*z
#これをSが最大となるようにyとLの式で表すと
# S_max = 1/2 * (L - y) * y * 1/2 * (L - y) = 1/4 * (y**3 - 2*L*y**2 +L**2 * y)

L = int(input())
S_list = []
for y in range(L*10**3):
    y_cal = y / 10**3
    s  = 1/4 * (y_cal**3 - 2*L*y_cal**2 +L**2 * y_cal)
    S_list.append(s)

S_max = max(S_list)
print(S_max)