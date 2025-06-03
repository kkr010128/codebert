n = int(input())
ans = 0
music = {}
for i in range(n):
    a, b = input().split()
    ans += int(b)
    music[a] = ans
print(ans-music[input()])

