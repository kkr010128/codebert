n = input()
a = [int(x) for x in input().split()]
print(' '.join(str(x) for x in a[::-1]))