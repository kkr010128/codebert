n,k = map(int,input().split())
person = [0]*n
for i in range(k):
    d = int(input())
    A = list(map(int,input().split()))
    for j in range(len(A)):
        person[A[j]-1] = 1
print(person.count(0))

