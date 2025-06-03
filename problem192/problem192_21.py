from copy import copy
from collections import Counter
n=int(input())
a=list(map(int,input().split()))
a_counter=Counter(a)
ans=0
for i in a_counter:
    ans+=(a_counter[i])*(a_counter[i]-1)//2
for j in a:
    true_ans=copy(ans)
    true_ans=true_ans-((a_counter[j])*(a_counter[j]-1)//2-(a_counter[j]-1)*(a_counter[j]-2)//2)
    print(true_ans)