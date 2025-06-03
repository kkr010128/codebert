n = int(input())
a_list = list(map(int, input().split()))
ans_list =[0]*n
for i in range(n):
    ans_list[a_list[i]-1] = i+1
print(*ans_list)