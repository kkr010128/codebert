S = input()
prev = ">"
terrain = []
curr = 0
for c in S:
    if c == prev:
        curr += 1
    else:
        prev = c
        terrain.append(curr)
        curr = 1
terrain += [curr]
ans = (terrain[0] * (terrain[0] + 1)) // 2
for up, down in zip(terrain[1::2], terrain[2::2]):
    if up < down:
        up, down = down, up
    down -= 1
    ans += (up * (up + 1)) // 2
    ans += (down * (down + 1)) // 2
if len(terrain) % 2 == 0:
    ans += terrain[-1] * (terrain[-1] + 1) // 2
print(ans)
