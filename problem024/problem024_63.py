n, k = map(int, input().split())
truck = [0] * k
w = []

for _ in range(n):
    w.append(int(input()))


def is_ok(p):
    truck_index = 0
    w_index = 0
    while w_index < n and truck_index < k:
        load_sum = 0
        while w_index < n and load_sum + w[w_index] <= p:
            load_sum += w[w_index]
            w_index += 1
        truck_index += 1
    return w_index == n


ng = 0
ok = 100000 * 100000

while ok - ng > 1:
    mid = (ng + ok) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print("%d" % ok)

