from collections import deque
n = int(input())
data = deque(list(input() for _ in range(n)))

ans = deque([])
co = 0

for i in data:
    if i[6] == ' ':
        if i[0] == 'i':
            ans.insert(0, i[7:])
            co += 1
        else:
            try:
                ans.remove(i[7:])
                co -= 1
            except:
                pass
    else:
        if i[6] == 'F':
            del ans[0]
            co -= 1
        else:
            del ans[-1]
            co -= 1

for i in range(0, co-1):
    print(ans[i], end=' ')
print(ans[co-1])
