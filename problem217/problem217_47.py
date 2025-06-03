N = int(input())
list_A = [int(m) for m in input().split()]

for i in list_A:
    if i % 2 != 0:
       continue
    elif not (i % 3 == 0 or i % 5 == 0):
            print("DENIED")
            exit()

else:
    print("APPROVED")