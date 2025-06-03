import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().rstrip().split())
inl = lambda: list(map(int, input().split()))
out = lambda x, s='\n': print(s.join(map(str, x)))

def check(a, b, c):
    if a == b or a == c or b == c:
        return False
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True

n = ini()
a = inl()
ans = 0
for i in range(n):
    for j in range(i+1, n):
        for t in range(j+1, n):
            if check(a[i], a[j], a[t]):
                ans += 1
print(ans)