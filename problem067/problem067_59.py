n = int(input())
T_point = 0
H_point = 0
for i in range(n):
    Taro, Hanako = input().split()
    if Taro > Hanako:
        T_point += 3
    elif Hanako > Taro:
        H_point += 3
    else:
        T_point += 1
        H_point += 1
print(T_point, H_point)