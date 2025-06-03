max_row, max_col = map(int, input().split(" "))
rows = [[0 for i in range(max_col)] for j in range(max_row)]
row = ""

for i in range(max_row):
    row =  input().split(" ")
    total_row = 0
    for j in range(max_col):
        rows[i][j] = int(row[j])
        total_row = total_row + int(row[j])
    rows[i].append(total_row)
    
#get summery of each columns
total = [0 for i in range(max_col+1)]
for m in range(max_col+1):
    for n in range(max_row):
        total[m] = total[m] + rows[n][m]
rows.append(total)


for i in range(max_row+1):
    out_str = ""
    for j in range(max_col+1):    
        out_str = out_str + " " + str(rows[i][j]) 
    
    print(out_str.strip())