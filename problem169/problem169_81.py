def abc163c_management():
    n = int(input())
    a = list(map(int, input().split()))
    cnts = [0] * n
    for v in a:
        cnts[v-1] += 1
    for v in cnts:
        print(v)
abc163c_management()