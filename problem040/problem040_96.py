a, b, c = map(int, input().split())

if a > b:
    tmp = b
    b = a
    a = tmp

if b > c:
    tmp = c
    c = b
    b = tmp

if a > b:
    tmp = b
    b = a
    a = tmp

print(a,b,c)

# sortを使って解く -> Presentation error となってしまう。。
"""
A = list(map(int, input().split()))
A.sort()
for a in A:
    print(a, end=' ')
"""

