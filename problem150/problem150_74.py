# カウントと踏破フラグをもっておくと二度目の踏破でループの長さが分かりそう

n, k = map(int, input().split())
a = list(map(lambda x: int(x) - 1, input().split()))
count_arr = [0] * n
count = 0

now = 0
loop_length = -1
while True:
    if count == k:
        print(now + 1)
        exit()
    if count_arr[now] != 0:
        loop_length = count - count_arr[now] + 1
        break
    count += 1
    count_arr[now] = count
    now = a[now]

# 真の残り回数
rest = (k - count) % loop_length

# 既にゴールしてると見る場合
if rest == 0:
    print(now + 1)
    exit()

while rest > 0:
    rest -= 1
    if rest == 0:
        break
    now = a[now]
print(a[now] + 1)
# 727202214173249352