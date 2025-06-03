X = int(input())

for i in range(1, 100001):
    if 100*i <= X <= 105*i:
        print(1)
        exit(0)
print(0)
