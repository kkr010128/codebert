# coding: utf-8

def showBuilding(mansion):
    for i, building in enumerate(mansion):
        for line in building:
            for room in line:
                print(' ' + str(room), end='')
            print()
        if i != 3:
            print('####################')

if __name__ == '__main__':
    mansion = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(4)]
    
    for _ in range(int(input())):
        b, f, r, v = map(int, input().split())
        mansion[b-1][f-1][r-1] += v

    showBuilding(mansion)

