health, attack = map(int, input().split())
damage = list(map(int, input().split()))
if health <= sum(damage):
    print('Yes')
else:
    print('No')