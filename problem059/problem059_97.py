r, c = list(map(int,input().split()))
S = [map(int,input().split()) for i in range(r)]
col_sum = [0 for i in range(c)];
for row in S:
    row = list(row)
    print(' '.join(map(str,row)) + ' {}'.format(sum(row)))
    col_sum = [x + y for (x,y) in zip(col_sum,row)]
print(' '.join(map(str,col_sum)) + ' {}'.format(sum(col_sum)))