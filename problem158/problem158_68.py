K = int(input())
A, B = [int(x) for x in input().split(" ")]

i = 1
while 1:
    if A <= i * K <= B:
        print("OK")
        break
    elif i * K > B:
        print("NG")
        break
    i += 1