# 視点を変えてやる全探索 000~999までが達成できたらおｋ
n = int(input())
s = list(input())
ans = 0
for i in range(1000):
    t = list(f"{i:0>3}")
    j = 0
    tmp = ""
    for c in s:
        if t[j] == c:
            j += 1
        if j == 3:
            ans += 1
            break
print(ans)