def solve(a, v, b, w, t):
    return "YES" if 0 < (v-w) and abs(b-a) / (v-w) <= t else "NO"

a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
print(solve(a, v, b, w, t))