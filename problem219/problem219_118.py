
N = input()
N = N[::-1]

c = 0
otsuri = 0
mai = 0
for i in range(len(N)):
    if int(N[i]) + c == 5 and i < len(N) - 1:
        if int(N[i+1]) >= 5:
            otsuri += 5
            c = 1
        else:
            mai += int(N[i]) + c
            c = 0
    elif int(N[i]) + c > 5:
        otsuri += 10 - int(N[i]) - c
        c = 1
    else:
        mai += int(N[i]) + c
        c = 0

print(otsuri + mai + c)