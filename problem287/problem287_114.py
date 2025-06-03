n = int(input())
for i in range(1,10):
    if n // i == n/i and n//i in range(1,10):
        print('Yes')
        break
else:
    print('No')