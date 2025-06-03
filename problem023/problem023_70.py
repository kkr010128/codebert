def insert(cnt, data):
    T[str(data)] = cnt


cnt = 0
T = {}
n = int(input())
for i in range(n):
    Order, data_S = input().split()
    if Order[0] =="i":
        insert(cnt, data_S)
        cnt +=1

    else:
        if str(data_S) in T:
            print("yes")
        else:
            print("no")
