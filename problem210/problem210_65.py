n = int(input())
S = input()
q = int(input())


class BIT:
    def __init__(self, n):
        """
        初期化
        Input:　
            n: 配列の大きさ
        """
        self.n = n
        self.bit = [0] * (n+10)

    def add(self, x, w):
        """
        更新クエリ(add)
        Input:
            x: インデックス
            w: 加える値
        Note:
            self.bitが更新される
        """        
        while x <= self.n:
            self.bit[x] += w
            x += x&-x
    
    def sum(self, x):
        """
        部分和算出クエリ
        Input:
            x: インデックス
        Return:
            [1,a]の部分和
        """
        cnt = 0
        while x > 0:
            cnt += self.bit[x]
            # 次の最下位桁はどこか
            x -= x&-x
        return cnt   
    
    def psum(self, a, b):
        """
        区間[a,b)(0-indexed)における和
        Input
            a,b: 半開区間
        Return
            [a,b)の和
        """
        return self.sum(b-1) - self.sum(a-1)


def str2num(s):
    return ord(s)-ord("a")

bits = [BIT(n) for i in range(26)]
# 入力
ans = []
for i, s in enumerate(S):
    ind = str2num(s)
    bits[ind].add(i+1, 1)

S = list(S)
for _ in range(q):
    x,a,b = input().split()
    if x == "1":
        i = int(a)
        # 更新処理
        ind_before = str2num(S[i-1])
        ind = str2num(b)
        bits[ind_before].add(i,-1)
        bits[ind].add(i, 1)
        S[i-1] = b
    else:
        l = int(a)
        r = int(b)
        cnt = 0
        for bit in bits:
            if bit.psum(l,r+1) > 0:
                cnt += 1
        ans.append(cnt)
print(*ans)

        
