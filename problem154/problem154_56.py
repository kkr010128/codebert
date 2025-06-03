N, K = map(int,input().split())

d_list = []
A_list = []

for i in range(K):
    d = int(input())
    d_list.append(d)
    A = list(map(int, input().split()))
    A_list.append(A)

person = [0 for i in range(N)]

for i in range(K):
    for j in range(d_list[i]):
        person[A_list[i][j]-1] += 1

print(person.count(0))