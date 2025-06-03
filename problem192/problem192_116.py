from collections import Counter
n = int(input())
a_input = list(map(int,input().split()))

a_count = Counter(a_input)

score_dic={}
exclude_dic={}

for k,v in a_count.items():
    score_dic[k]=v*(v-1)//2
    exclude_dic[k]=(v-1)*(v-2)//2

score_sum = sum(score_dic.values())

for i in range(n):
    print(score_sum-score_dic[a_input[i]]+exclude_dic[a_input[i]])
