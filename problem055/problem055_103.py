N = int(input())
residents = [[["0" for rooms in range(10)]for floor in range(3)]for builds in range(4)]

for i in range(N):
    b,f,r,v = list(map(int, input().split()))
    new_number = int(residents[b-1][f-1][r-1])+ v
    residents[b-1][f-1][r-1] = str(new_number)

for buils_num in range(4):
    for floor_num in range(3):
        print(' '+' '.join(residents[buils_num][floor_num]))
    if buils_num < 3:
        print('#'*20)