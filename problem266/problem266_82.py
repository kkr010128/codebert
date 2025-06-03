X = int(input())
for i in range(105, 100, -1):
    while True:
        if X % 100 < (X-i) % 100:
            break
        else:
            X = X-i
if X < 0: X = 1
print(1 if X % 100 == 0 else 0)
