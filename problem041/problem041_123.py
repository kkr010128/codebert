numbers = input()
numbers = numbers.split(" ")

W = int(numbers[0])
H = int(numbers[1])
x = int(numbers[2])
y = int(numbers[3])
r = int(numbers[4])

if (r <= x <= W - r) and (r <= y <= H - r):
    print("Yes")
else:
    print("No")