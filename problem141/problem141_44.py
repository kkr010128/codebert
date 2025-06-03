N = int(input())
A = list(map(int, input().split()))

node = 1
# 作成しなければならない葉の残りの数
leaf = sum(A)
max_node = 1
judge = True
ans = 0
for i, a in enumerate(A):
    ans += node
    leaf -= a
    if node < a+1 and leaf > 0:
        judge = False
        break
    # 次の深さのノード
    max_node = (node - a) * 2
    node = min(leaf, max_node)
    

if judge and max_node == 0:
    print(ans)
else:
    print(-1)
