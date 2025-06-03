import sys
from operator import itemgetter

sys.setrecursionlimit(5000)
input = sys.stdin.readline


TIME = 0
VAL = 1

N, T = [int(a) for a in input().split()]
time_value = [None] * (N + 1)
time_value[0] = (-1, -1)
for i in range(1, N + 1):
    time_value[i] = tuple(int(a) for a in input().split())

# Sort the array in the increasing order of value
time_value.sort(key = itemgetter(VAL))


# T by (N + 1) table for knapsack problem
# maximum possible time is T-1
dp_table = [[-1] * T for _ in range(N + 1)]

# Fill in dp_table i.e. solve knapsack problem
for t in range(0, T):
    dp_table[0][t] = 0

for n in range(1, N + 1):
    dp_table[n][0] = 0
    for t in range(1, T):
        if time_value[n][TIME] > t:
            dp_table[n][t] = dp_table[n - 1][t]
        else:
            dp_table[n][t] = max(dp_table[n - 1][t],
                             time_value[n][VAL] + dp_table[n - 1][t - time_value[n][TIME]])


val_acum = time_value[N][VAL]
t = T - 1
max_val = val_acum + dp_table[N - 1][t]

for n in range(N - 1, 0, -1):  # food to eat at the end
    val_acum += time_value[n][VAL] # value[N] + value[N-1] + ... + value[n]
    t -= time_value[n + 1][TIME] # T - 1 - (time[N] + time[N-1] + ... + time[n + 1])
    if t < 0: break
    tmp = val_acum + dp_table[n - 1][t]
    max_val = max(max_val, tmp)

print(max_val)