from collections import Counter

N = int(input())
A = [int(i) for i in input().split()]
cnt_list = Counter(A)

total = sum([cnt*(cnt-1)//2 if cnt > 1 else 0 for cnt in cnt_list.values()])
print(*[total-cnt_list[a]+1 for a in A], sep='\n')