n = int(input())
#a, b = map(int, input().split())
#l = list(map(int, input().split()))
#s = input()

for i in range(1,10):
    q, mod = divmod(n,i)
    if mod == 0:
        if (q >= 1 and q <= 9):
            print("Yes")
            exit()
print("No")


