while True:
    n, x = map(int, input().split())
    if not n and not x:
        break
    li = []
    for i in range(1,x//3):
        y = x - i
        li.append((y-1)//2 - max(i, y-n-1))
    print(sum([comb for comb in li if comb > 0]))