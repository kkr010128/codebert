N = int(input())
N_List = list(map(int,input().split()))
ct = 0
Current_Min = 2*(10**5) + 1
for i in range(N):
    if N_List[i] <= Current_Min:
        ct += 1
        Current_Min = N_List[i]
print(ct)