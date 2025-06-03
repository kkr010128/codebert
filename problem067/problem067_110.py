n = int(input())
t_p = 0
h_p = 0
for i in range(n):
    taro, hana = [i for i in input().split()]
    if taro > hana:
        t_p += 3
    elif taro == hana:
        t_p += 1
        h_p += 1
    else:
        h_p += 3
print(f'{t_p} {h_p}')
