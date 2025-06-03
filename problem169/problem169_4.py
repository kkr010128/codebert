n = int(input())
boss = list(map(int, input().split()))

subordinate = {}
for b in boss:
    subordinate[b] = subordinate.get(b, 0) + 1

for i in range(1, n+1):
    print(subordinate.get(i, 0))
