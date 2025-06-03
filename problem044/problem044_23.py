# coding: utf-8
# Here your code !
import sys

def culc_division(x) :
    """
    ??\???x????´???°?????°??????????????§??????
    """
    culc_list = []
    for i in range(1,x+1) :
        if x % i == 0 :
            culc_list.append(i)
            
    return culc_list
    
in_std = list(map(int, sys.stdin.readline().split(" ")))
a = in_std[0]
b = in_std[1]
c = culc_division(in_std[2])

counter = 0
for idx in range(a, b+1):
    if idx in c:
        counter += 1
        
print(counter)