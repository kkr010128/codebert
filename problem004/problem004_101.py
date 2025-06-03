n = int(input())

for i in range(n):
    a, b, c = list(map(int, input().split()))
    if min(a*a+b*b, min(a*a+c*c, c*c+b*b)) == max(a*a, max(b*b, c*c)):
        print ("YES")
    else:
        print ("NO")