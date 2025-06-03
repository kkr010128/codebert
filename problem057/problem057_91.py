while True:
    m, f, r = list(map(int, input().split()))

    if m == -1 and f == -1 and r == -1:
            break

    if (m == -1 or f == -1) or m+f < 30:
        print('F')
    elif 80 <= m+f:
        print('A')
    elif 65 <= m+f < 80:
        print('B')
    elif (50 <= m+f <65) or (30 <= m+f <50 and 50 <= r):
        print('C')
    elif 30 <= m+f <50:
        print('D')