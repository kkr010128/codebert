n = int(input())
nn = []
odd = 0
for i in range(1, n+1):
    if i % 2 == 1:
        odd += 1
    nn.append(i)
s = len(nn)
print(odd/s)
