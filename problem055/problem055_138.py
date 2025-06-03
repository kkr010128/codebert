# coding: utf-8

def showBuilding(mansion):
    for i, building in enumerate(mansion):
        for line in building:
            for room in line:
                print(' ' + str(room), end='')
            print()
        if i != 3:
            print('####################')

def calcMoving(mansion, moving_status):
    b, f, r, v = moving_status
    live_in_person = mansion[b-1][f-1][r-1]
    
    if live_in_person + v >= 9:
        live_in_person = 9
    elif live_in_person + v < 0:
        live_in_person = 0
    else:
        live_in_person += v
    
    mansion[b-1][f-1][r-1] = live_in_person

if __name__ == '__main__':
    mansion = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(4)]
    
    for _ in range(int(input())):
        calcMoving(mansion, map(int, input().split()))

    showBuilding(mansion)

