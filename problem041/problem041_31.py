num = list(map(int,input().split()))
 
circle_px = num[2] + num[4]
circle_mx = num[2] - num[4]

circle_py = num[3] + num[4]
circle_my = num[3] - num[4]

if(circle_px <= num[0] and circle_mx >= 0 and circle_py <= num[1] and circle_py >= 0): print("Yes")
else: print("No")
