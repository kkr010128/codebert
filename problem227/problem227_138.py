n, k = map(int, input().split())
enemy = list(map(int, input().split()))
enemy.sort(reverse=True)

if n <= k :
    print(0)
else :
    for i in range(k) :
        enemy[i] = 0
    print(sum(enemy))
