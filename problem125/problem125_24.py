x = int(input())
for i in range(360):
    if x*(i+1)%360 == 0:
        print(i+1)
        break