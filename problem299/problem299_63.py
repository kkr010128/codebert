n = int(input())
a = list(map(int, input().split()))

ans = [""]*n

for i in range(n):
    ans[a[i]-1] = str(i+1) #aのi番インデックスの値から１引いたものがans配列のインデックスになる。値は出席番号(i+1)

print(" ".join(ans))