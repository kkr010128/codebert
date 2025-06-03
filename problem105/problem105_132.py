n = int(input())
a = list(map(int, input().split()))

print(len(list(filter(lambda x: x % 2 == 1, a[::2]))))
