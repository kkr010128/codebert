input()
print(sum([int(x) % 2 for x in input().split()[::2]]))