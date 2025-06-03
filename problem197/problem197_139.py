from sys import stdin
#n = int(stdin.readline().rstrip())
#l = list(map(int, stdin.readline().rstrip().split()))
a,b,c = map(int, stdin.readline().rstrip().split())
#S = [list(map(int, stdin.readline().rstrip().split())) for _ in range(h)]#hの定義を忘れずに
import math
if c-a-b>0 and 4*a*b<(c-a-b)**2:
    print('Yes')
else:
    print("No")
