n = input()
p = [0] * 2
for i in range(n):
    t, h = raw_input().split()
    if(t > h):
        p[0] += 3
    elif(t < h):
        p[1] += 3
    else:
        p[0] += 1
        p[1] += 1
print("%d %d" %(p[0], p[1]))