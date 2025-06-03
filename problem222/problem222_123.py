# C - Distinct or Not
# https://atcoder.jp/contests/abc154/tasks/abc154_c

num = int(input())
p = list(map(int, input().split()))
list.sort(p)

ret = "YES"
for i in range(num-1):
    if p[i] == p[i+1]:
        ret = "NO"
        break

print("{}".format(ret))