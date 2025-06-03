f = list(map(int, input().split()))
q = int(input())
for i in range(q):
    a = list(map(int, input().split()))
    if a in [[f[0], f[1]], [f[1], f[5]], [f[5], f[4]], [f[4], f[0]]]:
        print(f[2])
    elif a in [[f[0], f[2]], [f[2], f[5]], [f[5], f[3]], [f[3], f[0]]]:
        print(f[4])
    elif a in [[f[0], f[4]], [f[4], f[5]], [f[5], f[1]], [f[1], f[0]]]:
        print(f[3])
    elif a in [[f[0], f[3]], [f[3], f[5]], [f[5], f[2]], [f[2], f[0]]]:
        print(f[1])
    elif a in [[f[1], f[2]], [f[2], f[4]], [f[4], f[3]], [f[3], f[1]]]:
        print(f[0])
    elif a in [[f[1], f[3]], [f[3], f[4]], [f[4], f[2]], [f[2], f[1]]]:
        print(f[5])
