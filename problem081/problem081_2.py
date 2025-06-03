input_list = [int(num) for num in input().split()]

D = input_list[0]
T = input_list[1]
S = input_list[2]

if D/S <= T:
    print("Yes")

else:
    print("No")