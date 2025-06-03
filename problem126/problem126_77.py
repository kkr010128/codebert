a = [x for x in range(1, 6)]
b = [int(x) for x in input().split()]

for i in range(5):
    if a[i] != b[i]:
        print(i+1)
