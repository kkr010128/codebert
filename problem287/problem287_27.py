N = int(input())
a = 0
for i in range(1,10):
    if N%i == 0 and N <= 9*i:
        print("Yes")
        a = 1
        break
if a == 0:
    print("No")