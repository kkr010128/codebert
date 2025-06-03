α = input()

small = "abcdefghijklmnopqrstuvwxyz"
ans = "A"
for i in range(len(small)):
    if α == small[i]:
        ans = "a"

print(ans)