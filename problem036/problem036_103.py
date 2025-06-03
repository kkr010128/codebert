import sys
input_line = sys.stdin.readline()
input_arr = input_line.split()
x = int(input_arr[0])
y = int(input_arr[1])
print str(x*y) + " " + str(2*x+2*y)