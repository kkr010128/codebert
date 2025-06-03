#ciが R のとき赤、W のとき白です。
#入力
#N
#c1...cN

N = int(input())
C = input()
Rednum = C.count('R')
#print(Rednum)
#Rの数 - 左にある赤の数が答
NewC = C[:Rednum]
#print(NewC)
Whinum = NewC.count('R')

print(Rednum - Whinum)
