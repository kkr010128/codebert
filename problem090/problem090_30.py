S = input()

if S[0] == 'R':
    if S[1] == 'R':
        if S[2] == 'R':
            print(3)
        else:
            print(2)
    else:
        print(1)
else:
    if S[1] == 'R':
        if S[2] == 'R':
            print(2)
        else:
            print(1)
    else:
        if S[2] == 'R':
            print(1)
        else:
            print(0)