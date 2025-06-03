a, b, c = map(int, input().split())
k = int(input())

ans = False

for i in range(k + 1):
    for j in range(k-i+1):
        for l in range(k-i-j+1):
            aa = a * pow(2,i)
            bb = b * pow(2,j)
            cc = c * pow(2,l)
            # print("{0} {1} {2}".format(aa,bb,cc))
            if(aa  < bb  and bb < cc):
                ans = True            

if(ans):
    print("Yes")
else:
    print("No")