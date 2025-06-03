from sys import stdin

a, b = (int(n) for n in stdin.readline().rstrip().split())

sign = "==" if a == b else ">" if a > b else "<"

print("a {} b".format(sign))

