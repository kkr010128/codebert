import math, itertools
from functools import reduce
def gcd_list(numbers):
    return(reduce(math.gcd,numbers))
k=int(input())
ans=0
for numbers in itertools.combinations_with_replacement(range(1,k+1),3):
    a,b,c=numbers
    if a==b==c:
        ans+=gcd_list(numbers)
    elif a!=b and a!=c and b!=c:
        ans+=6*gcd_list(numbers)
    else:
        ans+=3*gcd_list(numbers)
print(ans)