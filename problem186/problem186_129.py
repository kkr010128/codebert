#C - Traveling Salesman around Lake WA(ヒント)
K,N = map(int,input().split())
A = list(map(int, input().split()))

A[N+1:] = [A[0] + K]#Aを二回繰り返して円を表現

distance_list = []
for i in range(N):
    distance = abs(A[i] - A[i+1])
    distance_list.append(distance)
distance_list.remove(max(distance_list))
print(sum(distance_list))