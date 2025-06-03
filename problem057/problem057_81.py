m = 0
f = 0
r = 0

while(True):
    I = input().split()
    m = int(I[0])
    f = int(I[1])
    r = int(I[2])
    if m == -1 and f == -1 and r == -1:
        break
    score = m + f
    if m == -1 or f == -1:
        print('F')
        continue
    if score >= 80:
        print('A')
    if 65 <= score and score < 80:
        print('B')
    if 50 <= score and score < 65:
        print('C')
    if 30 <= score and score < 50:
        if r >= 50:
            print('C')
        else:
            print('D')
    if score < 30:
        print('F')