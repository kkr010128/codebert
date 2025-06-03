r = input()
if len(r) & 1:
    print("No")

else:
    for i in range(0, len(r), 2):
        if not (r[i] == 'h' and r[i + 1]=='i'):
            print("No")
            exit()
    print("Yes")