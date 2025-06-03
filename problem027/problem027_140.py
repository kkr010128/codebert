import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

N = int(input())
ans = []
const = 2*3**0.5
def korch_curve(Lx,Ly,Rx,Ry,i):
    if i == 0:
        ans.append((Lx,Ly))
        return 
    third_y = (Ly*2 + Ry)/3
    third_x = (Lx*2 + Rx)/3
    korch_curve(Lx,Ly,third_x,third_y,i - 1)
    middle_x = (Lx + Rx)/2 - (Ry - Ly)/const
    middle_y = (Ly + Ry)/2 + (Rx - Lx)/const
    korch_curve(third_x,third_y,middle_x,middle_y,i - 1)
    third_second_x = (Lx + Rx*2)/3
    third_second_y = (Ly + Ry*2)/3
    korch_curve(middle_x,middle_y,third_second_x,third_second_y,i - 1)
    korch_curve(third_second_x,third_second_y,Rx,Ry,i - 1)
korch_curve(0,0,100,0,N)
ans.append((100,0))
for a in ans:
    print(*a)
