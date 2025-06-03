#AGC039-A Connection and Disconnection
"""
sをk回繰り返して得られる文字列tを、全て隣り合う文字が異なるようにする
為に必要な操作回数を求めよ
解法：
最初と最後だけ愚直にカウント
あとは中間部分を連結してそれをk-1回繰り返す
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
s = readline().rstrip().decode('utf-8')
k = int(readline())
first = 0
last = 0
l = 0
r = len(s)

#全部同じ文字だとまずい
if len(set(s)) == 1:
    print(len(s)*k//2)
    exit()

if s[0] == s[-1]:
    res = s[0]
    for idx,i in enumerate(s):
        if i == res:
            first += 1
        else:
            l = idx
            break
    res = s[-1]
    for idx,i in enumerate(s[::-1]):
        if i == res:
            last += 1
        else:
            r = len(s)-idx
            break

count = 0
res = ""
for i in s[l:r]:
    if res == "":
        res = i
    elif res == i:
        count += 1
        res = ""
    else:
        res = i

print(first//2+last//2+(first+last)//2*(k-1)+count*k)