n , d = input() , 100000
for x in range(n):
        d += int(d*0.05)
        if d % 1000 != 0:
                d -= d % 1000
                d += 1000
print d