import numpy as np

N = int(input())
X = str(input())
num_one = X.count("1")

dp = [-1] * N
dp[0] = 0
def dfs(n):
    if dp[n] == -1:
        dp[n] = 1 + dfs(n % bin(n).count('1'))
    return dp[n]

num_one = X.count("1")
bool_arr = np.array([True if X[N-i-1] == "1" else False for i in range(N)])
zero_ver = np.array([pow(2,  i, num_one + 1) for i in range(N)])
zero_ver_sum = sum(zero_ver[bool_arr])

one_ver = -1
one_ver_sum = 0
flag = False
if num_one != 1:
    one_ver = np.array([pow(2,  i, num_one - 1) for i in range(N)])
    one_ver_sum = sum(one_ver[bool_arr])
else:
    flag = True
for i in range(1,N+1):
    start = 0
    if bool_arr[N-i] == False:
        start = (zero_ver_sum + pow(2, N - i, num_one + 1)) % (num_one + 1)
        print(dfs(start)+1)
    else:
        if flag:
            print(0)
        else:
            start = (one_ver_sum - pow(2, N - i, num_one - 1))  %  (num_one - 1)
            print(dfs(start)+1)
