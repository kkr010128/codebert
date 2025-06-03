def input_one():
	#no endline
	S1 = input()
	return S1

def x_cubic(num):
	return num**3

def output_line():
	print("")

def output(stdoutput):
	print(stdoutput, end = "")


output(x_cubic(int(input_one())))
output_line()