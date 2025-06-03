# 問題：https://atcoder.jp/contests/abc142/tasks/abc142_c

n = int(input())
a = list(map(int, input().strip().split()))
appear_attendance_number = {}
for i in range(n):
    appear_attendance_number[a[i]-1] = i+1
res = []
for i in range(n):
    res.append(appear_attendance_number[i])
print(' '.join(map(str, res)))

