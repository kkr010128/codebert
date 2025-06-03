W = raw_input()

S = []

while True:
    tmp = map(str, raw_input().split())
    if tmp[0] == "END_OF_TEXT":
        break
    else:
        S.append(tmp)

cnt = 0
for i in range(len(S)):
    for j in range(len(S[i])):
        if W == S[i][j].lower():
            cnt += 1

print cnt