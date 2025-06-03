import sys

class alphabet: #Trueなら大文字
    def __init__(self, capitalize):
        self.num = dict() #アルファベットを数字に変換
        self.abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"\
            ,"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        if capitalize: 
            for i in range(26): self.abc[i] = self.abc[i].upper()
        for i, a in enumerate(self.abc): self.num[a] = i


def solve():
    input = sys.stdin.readline
    N = int(input())
    S = input().strip("\n")
    Ans = ""
    Alphabet = alphabet(True)
    for i in range(len(S)):
        sNum = Alphabet.num[S[i]]
        rotateNum = (sNum + N) % 26
        Ans += Alphabet.abc[rotateNum]
    print(Ans)

    return 0

if __name__ == "__main__":
    solve()