import math
deg = int(input())
li_x = list(map(int,input().split()))
li_y = list(map(int, input().split()))
p1_dis = 0.0
p2_dis = 0.0
p2_temp = 0.0
p3_dis = 0.0
p3_temp = 0.0
p4_dis = 0.0
p4_temp = [ ]

for i in range(deg):
	p1_dis += math.fabs(li_x[i] - li_y[i])
	p2_temp += (li_x[i] - li_y[i]) **2.0
	p3_temp += math.fabs(li_x[i] - li_y[i]) **3.0
	p4_temp.append( math.fabs(li_x[i] - li_y[i]) )

p2_dis = math.sqrt( p2_temp )
p3_dis = math.pow(p3_temp, 1.0/3.0)
p4_dis = max(p4_temp)

print('{0:.6f}'.format(p1_dis))
print('{0:.6f}'.format(p2_dis))
print('{0:.6f}'.format(p3_dis))
print('{0:.6f}'.format(p4_dis))