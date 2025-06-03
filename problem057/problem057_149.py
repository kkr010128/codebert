score = []
while True:
    (m, f, r) = [int(i) for i in input().split()]
    if m == f == r == -1:
        break
    score.append([m, f, r])

for mc, fc, rc in score:
    if mc == -1 or fc == -1:
        print('F')
    elif mc + fc >= 80:
        print('A')
    elif mc + fc >= 65:
        print('B')
    elif mc + fc >= 50 or rc >= 50:
        print('C')
    elif mc + fc >= 30:
        print('D')
    else:
        print('F')