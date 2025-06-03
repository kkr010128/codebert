S=input()
lis=['SUN','MON','TUE','WED','THU','FRI','SAT']
i=lis.index(S)
if S=='SUN':
    print(7)
else:
    for j in range(1,8):
        if lis[i-j]=='SUN':
            print(7-j)
            break