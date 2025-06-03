y=100000
n = int(input())
for i in range(n):
    y=y*1.05
    if y%1000==0:
        pass
    else:
        y=y//1000
        y=y+1
        y=y*1000
print(f"{y:.0f}")
