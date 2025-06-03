a, b = [int(x) for x in input().split(" ")]
if a > b:
    ope =">"
elif a < b :
    ope ="<"
elif a == b:
    ope = "=="


print("a {} b".format(ope))