N,M = map(int, input().split())
A_list = [int(i) for i in input().split()]

playable_days = N - sum(A_list)

if playable_days >= 0:
    print(playable_days)
else:
    print("-1")