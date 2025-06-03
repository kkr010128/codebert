lst1 = input().split()

A = int(lst1[0])
B = int(lst1[1])
M = int(lst1[2])

list_A = input().split()
list_B = input().split()

for i in range(A):
   list_A[i] = int(list_A[i])

for i in range(B):
   list_B[i] = int(list_B[i])

result = min(list_A) + min(list_B)

list_M = []

for i in range(M):
   lst2 = input().split()
   n = list_A[int(lst2[0]) - 1] + list_B[int(lst2[1]) - 1] - int(lst2[2])
   if n < result:
      result = n

print(result)