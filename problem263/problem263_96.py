N = int(input())
A = list(map(int, input().split()))

mod = 10 ** 9 + 7
ans = 0
for i in range(60):
    ones = 0
    for a in A:
        # 数列Aの全要素の(二進法表記の)i桁目の１の数を集計する
        if a & (1 << i):
            ones += 1
    # Aの要素から任意の2つを選んで排他的論理和をとってできた数列をBとすると、
    # 数列Bの全要素のi桁目の合計は、(Aのi桁目の１の数)*(0の数)となる
    # 選んだ２つのAの要素が(0,1)の組み合わせになっている場合(XOR)だけに、Bの桁を構成する要素になるため
    ans = (ans + ones * (N - ones) * (1 << i)) % mod

print(ans)