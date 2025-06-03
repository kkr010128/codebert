x1, x2, x3, x4, x5 = map(int, input().split())
numbers = [x1,x2,x3,x4,x5]
for number in numbers:
    if number == 0:
        a = numbers.index(0)
        print(a + 1)
