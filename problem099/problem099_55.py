import math

def check(A, x, k):
    cut_count = 0
    for number in A:
        cut_count += (math.ceil(number / x)) -1
    return cut_count <= k

n, k = map(int,input().split())
a = list(map(int, input().split()))
ans = 0

l = 0
r = 10 ** 9
 
while r - l > 1:
    x = (r + l) // 2
  
    if check(a, x, k):
        r = x
    else:
        l = x   
print(r)