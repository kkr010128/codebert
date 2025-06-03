n = int(raw_input())
C = {'S':range(13), 'H':range(13), 'C':range(13), 'D':range(13)}

for i in range(n):
    suit, num = raw_input().split()
    num = int(num)
    C[suit][num-1] = 14

for i in ['S', 'H', 'C', 'D']:
    for j in range(13):
        if C[i][j] != 14:
            print "%s %d" %(i, j+1)