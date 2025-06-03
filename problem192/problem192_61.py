import collections

N = int(input())
A_list = list(map(int, input().split()))

c = collections.Counter(A_list)
c_value_list = list(c.values())
#print(c_value_list)

ans = 0

for i in range(len(c_value_list)):
    ans += c_value_list[i]*(c_value_list[i] - 1) // 2

for k in range(N):
    ans_temp = ans - c[A_list[k]] + 1
    print(ans_temp)
