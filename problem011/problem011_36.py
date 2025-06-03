import sys

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

# print(gcd(54, 20))
# print(gcd(147, 105))

input = sys.stdin.readline()
input = input.split(" ")
input = [int(i) for i in input]

print(gcd(input[0], input[1]))