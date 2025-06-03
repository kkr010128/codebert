import numpy as np

X = int(input())

x = np.arange(-300, 300, dtype=np.int64)

x5 = x**5
diff = np.subtract.outer(x5, x5)

i = np.where(diff == X)


x, y = i[0][0], i[0][1]
x -= 300
y -= 300

print(x, -y)
