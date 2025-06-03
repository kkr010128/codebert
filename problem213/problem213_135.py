N = int(input(""))
X = input("").split(" ")
X = [int(b) for b in X]
ans = 0
xb = int(round(sum(X) / len(X)))
for a in X:
    ans += (a-xb)**2
print(ans)