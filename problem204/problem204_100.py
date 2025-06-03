from collections import deque
# 両端を扱うならdequeが速い
# 内側を扱うならリストが速い

S = input()

q = deque()
for s in list(S):
    q.append(s)

Q = int(input())

direction = True

for _ in range(Q):
    line = input()

    # TrueならFalseに、FalseならTrueに変える
    if line == "1":
        direction = not direction

    else:
        if (direction and line[2] == '1') or (not direction and line[2] == '2'):
            # 左端に追加する場合
            q.appendleft(line[4])
        else:
            # 右端に追加する場合
            q.append(line[4])

if direction:
    print("".join(q))
elif not direction:
    q.reverse()
    print("".join(q))
