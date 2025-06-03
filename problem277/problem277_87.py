H, W, K = map(int, input().split())
cake = []
ans = [[0 for i in range(W)] for j in range(H)]
for i in range(H):
    cake.append(list(input()))


def change(i, j, count, count2, count3):
    #print(i, j, count,count2,  count3)
    for k in range(count2):
        for a in range(count):
            ans[i-k][j-a] = count3
stflag = 0
count2 = 0
count3 = 1
for i in range(len(cake)):
    count = 0
    stflag = 0
    for j in range(len(cake[i])):
        count += 1
        if cake[i][j] == "#":
            #print(i, j)
            change(i, j, count, count2 + 1, count3)
            count = 0
            count3 += 1
            stflag = 1
        if j == len(cake[i])-1:
            if stflag == 1:
                count3 -= 1
                change(i, j, count, count2 + 1, count3)
                count = 0
                count3 += 1
                count2 = 0
            else:
                count2 += 1

if count2 != 0:
    for i in range(count2):
        for j in range(len(cake[i])):
            ans[H - i - 1][j] = ans[H - count2 - 1][j]


for i in range(len(ans)):
    for j in range(len(ans[i])):
        print(ans[i][j], end=" ")
    print()