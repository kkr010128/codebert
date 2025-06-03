n = int(input())
T_p, H_p = 0, 0
for i in range(n):
    T, H = input().split()
    if T > H:
        T_p += 3
    elif T < H:
        H_p += 3
    else:
        T_p += 1; H_p += 1
print(T_p, H_p)

