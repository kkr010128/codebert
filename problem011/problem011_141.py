a, b = map(int, input().split())
c =1
if b > a:
    a, b = b, a
while c != 0:
    c = a % b
    a = b
    b = c
print(a)