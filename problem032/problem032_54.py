n = int(input())
x = [int(x) for x in input().split()]
y = [int(x) for x in input().split()]
abs_list = [abs(a-b) for a,b in zip(x,y)]
p1 = p2 = p3 = p4 = 0
for a in abs_list:
    p1 += a
    p2 += a**2
    p3 += a**3
p2 = p2 **(1/2)
p3 = p3 **(1/3)
p4 = max(abs_list)
preanswer = [p1,p2,p3,p4]
answer = ['{:.6f}'.format(i) for i in preanswer]
for a in answer:
    print(a)

