# 初期入力
import sys
input = sys.stdin.readline  #文字列では使わない
Standard=[400,600,800,1000,1200,1400,1600,1800,2000]
X = int(input())
from bisect import bisect_right
class_x =bisect_right(Standard,X)
print(9-class_x)
