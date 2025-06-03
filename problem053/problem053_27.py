n = input()
num = map(int, raw_input().split())

for i in range(n):
    if i == n-1:
        print num[n-i-1]
        break

    print num[n-i-1],