n, q = map(int, input().split())
array = [[s for s in input().split()] for i in range(n)]
total_time = 0
while len(array) != 0:
    a = array.pop(0)
    a_t = int(a[1])
    if a_t - q <= 0:
        total_time += a_t
        a[1] = total_time
        print(a[0], a[1])
    else:
        a[1] = a_t - q
        array.append(a)
        total_time += q