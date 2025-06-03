n = int(raw_input())
i = 1
print "",
for i in range(1,n+1):
    x = i
    if x%3 == 0:
        print "%d" %i ,
    elif x%10 == 3:
        print "%d" %i ,
    else:
        while x != 0:
            x = x/10
            if x % 10 == 3:
                print "%d" %i ,
                break