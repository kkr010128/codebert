#D - Chat in a Circle
N = int(input())
A = list(map(int,input().split()))
#ソート
arr = []
arr = sorted(A,reverse = True)

Friend_min_max_wa = 0
i =0
j = 0
for i in range(N -1):
    if i % 2 != 0 : j = j + 1
    Friend_min_max_wa = Friend_min_max_wa + arr[j]

# 出力
print(Friend_min_max_wa)