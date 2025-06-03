n = int(input())
a = list(map(int, input().split(" ")))
for lil_a in a[-1:0:-1]:
    print("%d "%lil_a, end="")
print("%d"%a[0])