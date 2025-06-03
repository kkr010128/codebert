N,K=map(int,input().split())
p_N = [int(i) for i in input().split()]
import heapq
print(sum(heapq.nsmallest(K,p_N)))
