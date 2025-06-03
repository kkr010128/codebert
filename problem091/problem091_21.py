import itertools
 
N = int(input())
L = list(map(int,(input().split())))
 
Combination = list(itertools.permutations(L, 3))
count = 0
for i in Combination:
    # a+b>c かつ b+c>a かつ c+a>b
    a = int(i[0])
    b = int(i[1])
    c = int(i[2])
    if((a+b)> c and (b+c) >a and (c+a) >b and a!=b and b!= c and a!= c and a<b and b<c):
        count+=1
 
print(count)