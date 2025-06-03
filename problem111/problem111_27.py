from collections import deque
N = int(input())
A = list(map(int,input().split()))
Query = deque()
A.sort(reverse=True)
Query.append([A[0],A[1]])
Query.append([A[0],A[1]])
Answer = A[0]
for i in range(2,N):
    query = Query.popleft()
    Answer += min(query)
    Query.append([max(query),A[i]])
    Query.append([min(query),A[i]])
print(Answer)