d = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(d)]
#t = [int(input()) for _ in range(d)]

TYPES = 26
history = [-1] * TYPES
satisfaction_level = [0] * (d+1)

def last(day, i, local_history):
    if local_history[i] == -1:
        return 0
    else:
        return local_history[i]

def satisfaction(day, typ):
    # コンテスト実施記録を更新
    local_history = list(history)
    local_history[typ] = day
    # 満足度の減少
    decrease = sum((c[i]*(day-last(day,i,local_history)) for i in range(TYPES)))
    value = s[day-1][typ] - decrease + satisfaction_level[day-1]
    return value

#for day, typ in enumerate(t):
#    print(satisfaction(day+1, typ-1))

for day in range(1, d+1):
    # 貪欲法
    greedy = max([(i+1, satisfaction(day, i)) for i in range(TYPES)], key=lambda x: x[1])
    history[greedy[0]-1] = day
    satisfaction_level[day] = greedy[1]
    print(greedy[0])
