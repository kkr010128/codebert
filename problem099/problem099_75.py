n, k = map(int, input().split())
a_i = list(map(int, input().split()))

def f(n):
    cnt = 0
    for a in a_i:
        cnt += (a - 1) // n
    if cnt > k: return False
    else: return True

l, r = 0, max(a_i)
while True:
    if r - l <= 1: break
    val = (l + r) // 2
    if f(val) == True: r = val
    else: l = val
print(r)