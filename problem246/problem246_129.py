def generate_arr(a):
    if len(a) == N:
        arr.append(a)
        return
    for i in range(1,N+1):
        if i not in a:
            generate_arr(a+[i])
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
arr = []
generate_arr([])
arr.sort()
ans_p = 0
ans_q = 0
for i in range(len(arr)):
    if arr[i] == P:
        ans_p = i+1
    if arr[i] == Q:
        ans_q = i+1
print(abs(ans_p-ans_q))