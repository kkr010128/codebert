n = int(input())
Taro = 0
Hanako = 0

for i in range(n):
    t,h = input().split()
    if t == h:
        Hanako += 1
        Taro += 1
    elif t> h:
        Taro += 3
    else:
         Hanako += 3
print("{} {}".format(Taro,Hanako))