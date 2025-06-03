s = input().split()
a = list(map(int, input().split()))
pos = s.index(input())
a[pos] -= 1
print(*a)
