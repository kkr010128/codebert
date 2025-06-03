input_list = map(int, raw_input().split())
ineq = ""
if input_list[0] < input_list[1]:
    ineq = "<"
elif input_list[0] > input_list[1]:
    ineq = ">"
else:
    ineq = "=="
print "a %s b" % (ineq)