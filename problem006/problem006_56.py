import sys

for num in sys.stdin:
    ini = 100000
    num = int(num)
    for i in range(1, num+1):
        ini = ini + ini*0.05
        mod = ini % 1000
        ini = ini - mod
        if mod != 0:
            ini += 1000
    ini = int(ini)
    print(ini)