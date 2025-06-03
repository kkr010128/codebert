S = input()
Q = int(input())
now = 1
head = ''
last = ''
for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        now = now * -1
    if query[0] == '2':
        if now * (int(query[1])-1.5) == 0.5:
            last += query[2]
        else:
            head += query[2]

ans = head[::-1] + S + last
if now == 1:
    print(ans)
else:
    print(ans[::-1])