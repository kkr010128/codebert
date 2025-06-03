n, a, b = map(int, input().split())

set_num = n // (a + b)
remain_num = n - (a + b) * set_num

print(set_num * a + min(remain_num, a))
