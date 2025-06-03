n = int(input())
can = False
for i in range(1, n + 1):
    x = int(i * 1.08)
    if(x == n):
        print(i)
        can = True
        break
if(can == False):
    print(":(")
