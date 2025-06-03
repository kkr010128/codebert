numbers = [int(i) for i in input().split()]
D, S, T = numbers[0], numbers[1], numbers[2]

if D <= S*T:
    print("Yes")
else:
    print("No")

