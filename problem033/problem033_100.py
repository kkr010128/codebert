#!/usr/bin/env python

label = list(map(int, input().split()))
command = list(input())

faces = [1, 2, 3, 4, 5, 6]


def dice(command):

    if command == "N":
        faces[0], faces[1], faces[4], faces[5] = faces[1], faces[5], faces[0], faces[4]

    elif command == "S":
        faces[0], faces[1], faces[4], faces[5] = faces[4], faces[0], faces[5], faces[1]

    elif command == "E":
        faces[0], faces[2], faces[3], faces[5] = faces[3], faces[0], faces[5], faces[2]

    else:  # command W
        faces[0], faces[2], faces[3], faces[5] = faces[2], faces[5], faces[0], faces[3]


for c in command:
    dice(c)

print(label[faces[0] - 1])

