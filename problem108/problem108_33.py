N = int(input())
for i in range(11):
    b = i * 1000
    c = b - N
    if c >= 0:
        break
print(c)