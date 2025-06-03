from collections import defaultdict
import math
import sys
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def main():
    MOD = 1000000007
    N = int(readline())
    m = map(int, read().split())
    A, B = zip(*zip(m, m))
    # Ai * Aj + Bi * Bj = 0
    # -> Ai * Aj = -Bi * Bj
    # -> (Ai/Bi) = -(Aj/Bj)
    # のとき、そのイワシ同士は入れられない

    # そこで、 Ci = Ai/Bi を約分したもの（かつBi>0としておく）
    # を覚えておき、Ci = -Cj となるようなペア同士を数えていく

    C = defaultdict(int)
    n00 = 0
    for a, b in zip(A, B):
        # (0, 0) はどのイワシとも仲が悪いので、考慮の対象から外して置き、
        # 後で(0, 0)のイワシの本数分足す
        if a == 0 and b == 0:
            n00 += 1
            continue

        # Bが0の場合、Aが0のイワシであればなんでも仲が悪くなるので、
        # C = -1 / 0 で統一する。
        if b == 0:
            C[(-1, 0)] += 1
            continue
        # Aが0の場合、Bが0のイワシであればなんでも仲が悪くなるので、
        # C = 0 / 1 で統一する。
        elif a == 0:
            C[(0, 1)] += 1
            continue
        # A / B を約分して、同じ値のイワシの個数を数え上げる
        g = math.gcd(a, b)
        a = a // g
        b = b // g
        # bは常に0以上にする
        if b < 0:
            b = -b
            a = -a
        C[(a, b)] += 1
    
    C = dict(C)
    flag = {k: False for k in C.keys()}

    ans = 1
    for c, nc in C.items():
        a, b = c
        a2, b2 = (-b, a) if a >= 0 else (b, -a)
        # 仲の悪いイワシの個数
        nBad = C.get((a2, b2), 0)
        # 仲の悪いイワシがいなければ、
        # この中からイワシを選ぶ時のすべての組み合わせ（全て選択しない場合を含む）の数を考える
        # = 2^nc  = 1 << nc
        if nBad == 0:
            k = 1 << nc
        else:
            # (-2, 3) (3, 2) があるとき、それぞれで組み合わせを考えると重複するので、
            # 片方しか数えないようにする
            if flag[(a2, b2)]:
                continue

            # 仲の悪いイワシがいる場合、
            # あるCのイワシがnc本、それと中の悪いイワシがnBad本あるとする。
            # nc + nBad 本のイワシのうち、OKな組み合わせの個数は
            # [nc本から1本以上選ぶ組み合わせ] + [nc本から1本以上選ぶ組み合わせ] + [イワシを全て選択しない場合]
            # (2^nc - 1) + (2^nBad - 1) + 1 = 2^nc + 2^nBad - 1
            k = (1 << nc) + (1 << nBad) - 1
        
        ans = (ans * k) % MOD
        flag[c] = True

    # 上の数え上げだと、イワシを1本も選ばない場合も含まれているので、
    # そのパターンを除外するため-1する。
    # -1 するついでに(0, 0) のイワシから1本以上選ぶ場合の数も足しておく
    ans = (ans + n00 - 1) % MOD
    print(ans)


if __name__ == '__main__':
    main()