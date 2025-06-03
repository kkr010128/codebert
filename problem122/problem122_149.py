def SUM(num_List):
    answer = 0
    for i, num in enumerate(num_List):
        answer += num*i
    return answer

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = list()
C = list()
start = True

num_List = [0 for x in range(100001)]

for a in A:
    num_List[a] = num_List[a] + 1

for x in range(Q):
    b, c = map(int, input().split())
    B.append(b)
    C.append(c)

for x in range(Q):
    b = B[x]
    c = C[x]

    if start == True:
        num_List[c] = num_List[c] + num_List[b]
        num_List[b] = 0
        answer = SUM(num_List)
        start = False
        
    else:
        answer = answer + num_List[b]*(c-b)
        num_List[c] = num_List[c] + num_List[b]
        num_List[b] = 0

    print(answer)