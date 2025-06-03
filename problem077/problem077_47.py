import numpy as np
a, b, c, d = map(int, input().split())

hoge = []
hoge.append(a*c)
hoge.append(a*d)
hoge.append(b*c)
hoge.append(b*d)

print(max(hoge))