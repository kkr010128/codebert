r,c = map(int, raw_input().split())

col_sum = [0] * (c+1)
for i in range(r):
    row = map(int, raw_input().split())
    row.append(sum(row))
    col_sum = [a + b for a, b in zip(row, col_sum)]
    
    print " ".join(map(str, row))
    
print " ".join(map(str, col_sum))