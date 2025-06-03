from operator import itemgetter
faces = list(map(int, input().split()))
commands = input()

for command in commands:
    if command == 'N':
        faces = itemgetter(1,5,2,3,0,4)(faces)
    elif command == 'E':
        faces = itemgetter(3,1,0,5,4,2)(faces)
    elif command == 'S':
        faces = itemgetter(4,0,2,3,5,1)(faces)
    elif command == 'W':
        faces = itemgetter(2,1,5,0,4,3)(faces)
print(faces[0])
