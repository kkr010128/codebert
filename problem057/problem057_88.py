while True:
    x, y, z = map(int, input().split())
    if x == -1 and y == -1 and z == -1:
        break
    if x == -1 or y == -1:
        print ('F')
    elif x + y >= 80:
        print ('A')
    elif 65 <= x+y < 80:
        print ('B')
    elif 50 <= x+y < 65 or (30 <= x+y < 50 and z >= 50):
        print ('C')
    elif 30 <= x+y < 50:
        print ('D')
    elif x + y < 30:
        print ('F')
