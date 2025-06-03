import numpy as np

a,b,h,m=list(map(int,input().split()))

deg = min(abs(h*360/12+m*360/12/60-m*360/60),360-abs(h*360/12+m*360/12/60-m*360/60))
theta = deg * np.pi /180
ans = np.sqrt(np.power(a,2)+np.power(b,2)-2*a*b*np.cos(theta))

print(ans)