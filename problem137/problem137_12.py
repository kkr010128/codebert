N = int(input())
A_list = []
B_list = []
for i in range(N):
    A, B = map(int, input().split())
    A_list.append(A)
    B_list.append(B)
sort_A = sorted(A_list)
sort_B = sorted(B_list)

if N % 2 == 0:
    center_A = (sort_A[N//2] + sort_A[N//2-1])/2
    center_B = (sort_B[N//2] + sort_B[N//2-1])/2
    print(int((center_B-center_A)*2)+1)
else:
    center_A = sort_A[N//2]
    center_B = sort_B[N//2]
    print(center_B-center_A+1)