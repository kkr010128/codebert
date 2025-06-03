input()
bits = 1
for a in map(int, input().split()): bits |= bits << a
input()
print(*("yes"*((bits >> q) & 1)or"no" for q in map(int, input().split())), sep='\n')