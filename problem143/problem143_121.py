
k = int(input())
s = str(input())

if len(s) > k:
    print(s[:k], end='')
    print("...")
else:
    print(s)
