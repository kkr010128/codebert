import sys
printf = sys.stdout.write

bilt1 = [0] * 30
bilt2 = [0] * 30
bilt3 = [0] * 30
bilt4 = [0] * 30

sha = "#" * 20
count = 0;

x = input()
for i in range(x):
    b,f,r,v =map(int, raw_input().split())
    if b == 1:
        bilt1[((f - 1) * 10) + (r - 1)] = bilt1[((f - 1) * 10) + (r - 1)] + v
    elif b == 2:
        bilt2[((f - 1) * 10) + (r - 1)] = bilt2[((f - 1) * 10) + (r - 1)] + v
    elif b == 3:
        bilt3[((f - 1) * 10) + (r - 1)] = bilt3[((f - 1) * 10) + (r - 1)] + v
    else:
        bilt4[((f - 1) * 10) + (r - 1)] = bilt4[((f - 1) * 10) + (r - 1)] + v

for i in range(3):
    for j in range(10):
        print " ",
        printf(str(bilt1[(i * 10) + j]))
    print ""
print sha

for i in range(3):
    for j in range(10):
        print " ",
        printf(str(bilt2[(i * 10) + j]))
    print ""
print sha

for i in range(3):
    for j in range(10):
        print " ",
        printf(str(bilt3[(i * 10) + j]))
    print ""
print sha

for i in range(3):
    for j in range(10):
        print " ",
        printf(str(bilt4[(i * 10) + j]))
    print ""