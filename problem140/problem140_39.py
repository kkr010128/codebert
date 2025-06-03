t = input('')

tlist = list(t)
for i in range(len(tlist)):
    if tlist[i] == '?':
        if i==0:
            tlist[i] = 'D'
        elif i==len(tlist)-1:
            tlist[i] = 'D'
        else:
            if tlist[i-1] == 'P':
                if tlist[i+1] == 'P':
                    tlist[i] = 'D'
                elif tlist[i+1] == 'D':
                    tlist[i] = 'D'
                elif tlist[i+1] == '?':
                    tlist[i] = 'D'
            else:
                # 1つ前が'D'
                if tlist[i+1] == 'P':
                    tlist[i] = 'D'
                elif tlist[i+1] == 'D':
                    tlist[i] = 'P'
                elif tlist[i+1] == '?':
                    tlist[i] = 'P'

print("".join(tlist))