a, b = map(int, input().split(" "))

tmp_str = ""
if a==b:
    tmp_str = " == "
elif a > b:
    tmp_str = " > "
else:
    tmp_str = " < "

print("a" + tmp_str + "b")