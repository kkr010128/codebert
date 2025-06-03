n = int(input())
a = [int(i) for i in input().split()]

print(' '.join(map(str, reversed(a))))