c = input()
l = list('abcdefghijklmnopqrstuvwxyz')

for i in range(0, len(l)):
    if c == l[i]:
        print(l[i+1])
    else:
        i+=1