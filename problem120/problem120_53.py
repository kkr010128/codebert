N, K = map(int, input().split())
p_list = list(map(int, input().split()))
 
p_list = sorted(p_list)
 
print(sum(p_list[:K]))