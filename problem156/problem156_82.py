X = int(input())


for a in range(-118,120):
    for b in range(-119,119):
        if a**5 - b**5 == X:
            ans = (a,b)
            break

print(ans[0],ans[1])
