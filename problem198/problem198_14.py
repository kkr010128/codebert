import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

N = int(input())

lst1 = [('a', 0)]
lst2 = []
for i in range(N - 1):
    if i % 2 == 0: #lst1 -->lst2
        lst2 = []
        for s, t in lst1:
            last = max(ord(s[i]) - ord('a'), t)
            for j in range(last + 2):
                lst2.append((s + chr(j + ord('a')), max(t, j)))
    else:
        lst1 = []
        for s, t in lst2:
            last = max(ord(s[i]) - ord('a'), t)
            for j in range(last + 2):
                lst1.append((s + chr(j + ord('a')), (max(t, j))))
           
if len(lst2) > len(lst1):
    lst2.sort()
    for s, t in lst2:
        print (s)
else:
    lst1.sort()
    for s, t in lst1:
        print (s)