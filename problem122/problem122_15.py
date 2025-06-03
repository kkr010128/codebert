N = int(input())
A = list(map(int, input().split()))
Q = int(input())
BC_List = x = [list(map(int, input().split())) for i in range(Q)]

int_list = [0 for _ in range(10**5+1)]
sum = 0
for i in A:
   int_list[i] += 1
   sum += i

for B, C in BC_List:
    sum = sum + (C-B) * int_list[B]
    int_list[C] += int_list[B]
    int_list[B] = 0
    print(sum)
