n, k, c = map(int, input().split())
s = input()
left_dp = []
right_dp = []

i = 0
while len(left_dp)<k:
    if s[i] == "o":
        left_dp.append(i+1)
        i += c+1
    else: i += 1
        
i = n-1
while len(right_dp)<k:
    if s[i] == "o":
        right_dp.append(i+1)
        i -= c+1
    else: i -= 1

for i in range(k):
    if left_dp[i] == right_dp[k-i-1]:
        print(left_dp[i])