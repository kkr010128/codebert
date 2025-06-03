import math

while True:
    n = int(input())
    if(n == 0):
        exit()
    else:
        s = [int(x) for x in input().split()]
        m = sum(s)/len(s)

        for i in range(n):
            s [i] = (s[i] - m)**2

        print("%.5f" % (math.sqrt(sum(s)/len(s))))