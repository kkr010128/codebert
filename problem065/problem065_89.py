
W = input()
count = 0
T = input()
#print(T)
while T != 'END_OF_TEXT':
    for i in T.lower().split():
        if W == i:
            count += 1
    T = input()
    #print(i)

print(count)