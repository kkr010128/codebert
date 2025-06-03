while True:
    m = map(int,raw_input().split())
    if m[0] == 0 and m[1] == 0:
        break
    if m[0] >= m[1]:
        print m[1],m[0]
    else:
        print m[0],m[1]