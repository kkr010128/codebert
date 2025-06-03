r = lambda:map(int, input().split())
a, v = r()
b, w = r()
print("YES" if int(input())*(v-w) >= abs(b-a) else "NO")