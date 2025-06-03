numbers = [int(x) for x in input().split(" ")]
a, b = numbers[0], numbers[1]
print("{} {} {:.5f}".format((a//b), (a%b), (a/b)))