def judge(m, f, r):
    p = m + f
    if (m == -1 or f == -1 or p < 30):
        a = 'F'
    elif (p >= 80):
        a = 'A'
    elif (p >= 65 and p < 80):
        a = 'B'
    elif (p >= 50 and p < 65 or r >= 50):
        a = 'C'
    elif (p >= 30 and p < 50):
        a = 'D'
    return a

while True:
    m, f, r = map(int, input().split())
    if (m == -1 and f == -1 and r == -1):
        break
    print(judge(m, f, r))