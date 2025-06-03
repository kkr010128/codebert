#　動的計画法で求める
s = int(input())
mod = 10 ** 9 + 7
A = [0, 0, 0, 1, 1, 1, 2, 3]
for i in range(8, 2000 + 1):
    ans = (sum(A[:i - 3 + 1]) + 1) % mod #Aの先頭からi-3+1までを取得
    A.append(ans)#配列に結果を加える
print(A[s])