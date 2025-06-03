h, w, k = list(map(int, input().split()))
m = [list(input()) for _ in range(h)]
ans = 0

for bh in range(1 << h):
    for bw in range(1 << w):
        B = 0
        for H in range(h):
            for W in range(w):
                if ((bh >> H) & 1) == 0 and ((bw >> W) & 1) == 0 and m[H][W] == "#":
                    B += 1
        if B == k:
            ans += 1
print(ans)
