ls = sorted(list(map(int,input().split())))
if ls[0] == ls[1] and ls[0] != ls[2]:
    print('Yes')
elif ls[1] == ls[2] and ls[0] != ls[1]:
    print('Yes')
elif ls[0] == ls[2] and ls[0] != ls[1]:
    print('Yes')
else:
    print('No')