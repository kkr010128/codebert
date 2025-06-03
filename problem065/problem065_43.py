import fileinput
W = input()
cnt = 0
for T in fileinput.input():
    if T.rstrip() =='END_OF_TEXT':
        break

    T = T.lower().split()
    cnt += T.count(W)
    # print(T, cnt)
print(cnt)

