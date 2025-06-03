#axino's copy

def move(up, bottom, right, left, front, back, direction):
    if direction == 'N':
        return(front, back, right, left, bottom, up)
    elif direction == 'S':
        return(back, front, right, left, up, bottom)
    elif direction == 'E':
        return(left, right, up, bottom, front, back)
    elif direction == 'W':
        return(right, left, bottom, up, front, back)

def check(up, bottom, right, left, front, back, up_current, front_current):
    if front_current == front and up_current == up:
        print(right)
    elif front_current == front:
        if left == up_current:
            print(up)
        elif bottom == up_current:
            print(left)
        elif right == up_current:
            print(bottom)
    elif up_current == up:
        if right == front_current:
            print(back)
        elif back == front_current:
            print(left)
        elif left == front_current:
            print(front)
    else:
        up, bottom, right, left, front, back = move(up, bottom, right, left, front, back, 'S')
        check(up, bottom, right, left, front, back, up_current, front_current)
up, front, right, left, back, bottom = input().split()
times = int(input())

for i in range(times):
    up_current, front_current = input().split()
    check(up, bottom, right, left, front, back, up_current, front_current)