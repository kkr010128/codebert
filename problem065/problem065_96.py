W = input()
count = 0
#T = input().lower()
#print(T)
#while T != 'END_OF_TEXT':
while True:
    T = input()
    if T == 'END_OF_TEXT':
        break

    for i in T.lower().split():
        if W == i:
            count += 1
    #T = input().lower()
    #print(i)

print(count)