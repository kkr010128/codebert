n = int(input())
cout = ""
for i in range(1,n+1):
    x = i
    if x%3 == 0:
        cout += " " + str(i)
    else:
        while x > 0:
            if x%10 == 3:
                cout += " " + str(i)
                break
            x //= 10
print (cout)