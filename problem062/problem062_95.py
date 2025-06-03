X = []
while True:
    x = raw_input()
    if x == "0":
        break
    else:
        X.append(x)

ans = []
for i in range(len(X)):
    tmp = 0
    for j in range(len(X[i])):
        tmp+=int(X[i][j])
    ans.append(tmp)

for char in ans:
    print char
