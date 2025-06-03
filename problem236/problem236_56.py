h, w, n = map(int, [input() for _ in range(3)])
print((n-1)//max(h, w)+1)