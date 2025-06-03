d = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(d)]
t = [int(input()) for _ in range(d)]

TYPES = 26
history = [-1] * TYPES
satisfaction_level = [0] * (d+1)

def last(day, i):
    if history[i] == -1:
        return 0
    else:
        return history[i]

def satisfaction(day, typ):
    # コンテスト実施記録を更新
    history[typ] = day
    # 満足度の減少
    decrease = sum((c[i]*(day-last(day,i)) for i in range(TYPES)))
    value = s[day-1][typ] - decrease + satisfaction_level[day-1]
    satisfaction_level[day] = value
    return value

for day, typ in enumerate(t):
    print(satisfaction(day+1, typ-1))