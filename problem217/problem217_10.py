# B - Papers, Please
# https://atcoder.jp/contests/abc155/tasks/abc155_b

n = int(input())
a = list(map(int, input().split()))

even = 0
cnt = 0

for i in a:
    if i % 2 == 0:
        even += 1
        if i % 3 == 0 or i % 5 == 0:
            cnt += 1

if even == cnt:
    print('APPROVED')
else:
    print('DENIED')
