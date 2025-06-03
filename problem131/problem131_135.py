a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

d = abs(a-b)
s = v-w
if s <= 0: print("NO"); exit()

print("YES" if d <= t * s else "NO")
