scores = []
while True:
    a_score = [int(x) for x in input().split( )]
    if a_score[0] == a_score[1]  == a_score[2] == -1:
        break
    else:
        scores.append(a_score)
for s in scores:
    m,f,r = [int(x) for x in s]
    if m == -1 or f == -1:
        print('F')
    elif m + f >= 80:
        print('A')
    elif m + f >= 65:
        print('B')
    elif m + f >= 50 or r >= 50:
        print('C')
    elif m + f >= 30:
        print('D')
    else:
        print('F')

