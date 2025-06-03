H = int(input())
p = 0
for i in range(50):
    if 2**i <= H and H < 2**(i + 1):
        p = i
        break
# print(p)
print(2**(p + 1) - 1)
