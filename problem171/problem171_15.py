N = int(input())
A_list = map(int, input().split())
 
# [活発度, もとの番号] のリストを降順に並べる
A_list = [[A, index] for index, A in enumerate(A_list)]
A_list.sort(reverse=True)
 
# print(A_list)
 
dp = [[0 for i in range(N+1)] for j in range(N+1)]
# print(dp)
for left in range(0, N):
    for right in range(0, N - left):
        # print(f'left, righte: { left, right }')
        # print(A_list[left + right - 1][0])
        activity = A_list[left + right][0]
        distance_from_left = A_list[left + right][1] - left
        # print(f'distance_from_left: { distance_from_left }')
        distance_from_right = (N - 1 - right) - A_list[left + right][1]
        # print(f'distance_from_right: { distance_from_right }')
        dp[left + 1][right]\
            = max(dp[left + 1][right],
                  dp[left][right] + activity * distance_from_left)
        dp[left][right + 1]\
            = max(dp[left][right + 1],
                  dp[left][right] + activity * distance_from_right)
        # print('dp---')
        # print(dp)
        # print('---dp')
# print(dp)
dp_list = [flatten for inner in dp for flatten in inner]
print(max(dp_list))