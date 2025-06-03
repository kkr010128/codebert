def roll(l, command):
    '''
    return rolled list

    l : string list
    command: string
    '''
    res = []
    i = -1
    if command =='N':
        res = [l[i+2], l[i+6], l[i+3], l[i+4], l[i+1], l[i+5]]
    if command =='S':
        res = [l[i+5], l[i+1], l[i+3], l[i+4], l[i+6], l[i+2]]
    if command =='E':
        res = [l[i+4], l[i+2], l[i+1], l[i+6], l[i+5], l[i+3]]
    if command =='W':
        res = [l[i+3], l[i+2], l[i+6], l[i+1], l[i+5], l[i+4]]

    return res

faces = input().split()
commands = list(input())

for command in commands:
    faces = roll(faces, command)

print(faces[0])

