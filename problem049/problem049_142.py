ans = []


def paint(h, w):
    ans.append("\n".join(["#" * w] * h))


while True:
    H, W = map(int, input().split())
    if H == W == 0: break

    paint(H, W)

print(("\n" * 2).join(ans), "\n", sep = "")
