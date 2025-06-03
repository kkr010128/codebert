A, B, C, D = map(int, input().split())

while True:
    C -= B
    if C < 1:
        print('Yes')
        quit()
    A -= D
    if A < 1:
        print('No')
        quit()
