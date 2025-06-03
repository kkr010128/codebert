suit = ['S','H','C','D']
num = range(0, 13)
deck = {'S':[0]*13, 'H':[0]*13, 'C':[0]*13, 'D':[0]*13} 

n = input()
 
for i in range(0, n):
    a, b = raw_input().split(" ")
    deck[a][int(b)-1] = 1
 
for i in suit:
    for j in num:
        if (deck[i][j] == 0):
            print("%s %d" % (i, j+1))