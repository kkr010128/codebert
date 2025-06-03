# -*- coding: utf-8 -*-


def simu(pro, q):
    end_time = 0

    while bool(pro):
        if pro[1] > q:
            end_time += q
            pro.append(pro[0])
            pro.append(pro[1] - q)
            pro.pop(0)
            pro.pop(0)

        elif pro[1] <= q:
            end_time += pro[1]
            print('{0} {1}'.format(pro[0], end_time))
            pro.pop(0)
            pro.pop(0)


n, q = list(map(int, input().split()))

pro = []
for i in range(n):
    name, time = list(input().split())
    pro.append(name)
    pro.append(int(time))

simu(pro, q)

