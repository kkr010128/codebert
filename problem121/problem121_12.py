n = int(input())
#a, b, h, m = map(int, input().split())
#al = list(map(int, input().split()))
#al=[list(input()) for i in range(h)]

l = 1
total = 26

while n > total:
    l += 1
    total += 26**l

last = total-26**l
v = n-last-1

ans = ''
# 26進数だと見立てて計算
for i in range(l):
    c = v % 26
    ans += chr(ord('a')+c)
    v = v//26
print("".join(ans[::-1]))
