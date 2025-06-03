m, n = map(int, input().split())
sheet = [ list(map(int, input().split())) for i in range(m)]
for i in range(m):
    sheet[i].append(sum(sheet[i]))
    if i == 0:
        sheet.append(list(sheet[i]))
    else :
        for j in range(n):
            sheet[-1][j] += sheet[i][j]
sheet[-1][-1] = sum(sheet[-1]) - sheet[0][-1]
for tmp_list in sheet:
    print(" ".join(str(x) for x in tmp_list))