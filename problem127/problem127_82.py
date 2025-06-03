X, Y = [int(v) for v in input().split()]

ans = "No"
for c in range(X + 1):
    t = X - c
    if 2 * c + 4 * t == Y:
        ans = "Yes"
        break
# if ans == "No":
#     for t in range(X + 1):
#         c = X - t
#         if 2 * c + 3 * t == Y:
#             ans = "Yes"
#             break

print(ans)