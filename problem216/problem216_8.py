a, b, c = map(int, input().split())
ret = "No"
if (a == b and a != c) or (b == c and c != a) or (c == a and a != b):
    ret = "Yes"

print("{}".format(ret))