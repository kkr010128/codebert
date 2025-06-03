cnt = int(input())
dif_max = -1000000000
v_min = 1000000000

for i in range(cnt):
    buf = int(input())
    if i > 0:
        dif_max = dif_max if buf - v_min < dif_max else buf - v_min
    v_min = buf if buf < v_min else v_min
print(dif_max)