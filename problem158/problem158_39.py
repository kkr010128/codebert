K = int(input())

A, B = map(int, input().split())

check = A
#print(check%K)

while check <= B:
    if check%K == 0:
        print("OK")
        exit()
    else:
        check += 1

print("NG")
