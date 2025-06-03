from collections import Counter
import itertools
n=int(input())
rgb=list(input())
rgb_counter=Counter(rgb)
n_list=[i for i in range(1,n+1)]
count=0
for i,j in itertools.combinations(n_list,2):
    k=2*j-i
    if k<=n and rgb[j-1]!=rgb[i-1] and rgb[j-1]!=rgb[k-1] and rgb[i-1]!=rgb[k-1]:
        count+=1
print(rgb_counter["R"]*rgb_counter["G"]*rgb_counter["B"]-count)
