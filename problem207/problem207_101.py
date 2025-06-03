a=[]
for i in range(3):
    a.append(list(map(int, input().split())))

n=int(input())

b=[]
for i in range(n):
    b.append(int(input()))

for bingo in b:
    for gyou in range(3):
        for retu in range(3):
            if a[gyou][retu]==bingo:
                a[gyou][retu]=True

if a[0][0]==True and a[0][1]==True and a[0][2]==True:
    print("Yes")
    exit()
elif a[1][0]==True and a[1][1]==True and a[1][2]==True:
    print("Yes")
    exit()
elif a[2][0]==True and a[2][1]==True and a[2][2]==True:
    print("Yes")
    exit()
elif a[0][0]==True and a[1][0]==True and a[2][0]==True:
    print("Yes")
    exit()
elif a[0][1]==True and a[1][1]==True and a[2][1]==True:
    print("Yes")
    exit()
elif a[0][2]==True and a[1][2]==True and a[2][2]==True:
    print("Yes")
    exit()
elif a[0][0]==True and a[1][1]==True and a[2][2]==True:
    print("Yes")
    exit()
elif a[0][2]==True and a[1][1]==True and a[2][0]==True:
    print("Yes")
    exit()

print("No")