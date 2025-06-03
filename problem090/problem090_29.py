S = input()
zenzitsu = False

ans = 0
for i in range(len(S)):
    if S[i] == "R":
        if zenzitsu:
            ans += 1
            zenzitsu = True
        else:
            ans = 1
            zenzitsu = True
    else:
        zenzitsu = False
print(ans)