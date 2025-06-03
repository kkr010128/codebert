st = list()
while True:
    a = list(map(lambda x: int(x),input().split(" ")))
    if min(a[0:2]) == -1:
        if max(a) == -1:
            break
        else:
            st += {"F"}
    else:
        if 80 <= sum(a[0:2]):
            st += {"A"}
        elif 65 <= sum(a[0:2]):
            st += {"B"}
        elif 50 <= sum(a[0:2]):
            st += {"C"}
        elif 30 <= sum(a[0:2]):
            if 50 <= a[2]:
                st += {"C"}
            else:
                st += {"D"}
        else:
            st += {"F"}
    
for s in st:
    print(s)