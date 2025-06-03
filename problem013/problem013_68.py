# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_D
sample_input = '''
3
4
3
2
'''
give_sample_input = False
if give_sample_input:
  sample_input_list = sample_input.split()
  def input():
    return sample_input_list.pop(0)

numOfData = int(input())
max_diff = None  # minus infty
min_val = None  # plus infty
prev_val = int(input())
for n in range(numOfData-1):
	val = int(input())
	if min_val is None:
		min_val = prev_val
	else:
		min_val = min(prev_val, min_val)
	if max_diff is None:
	  max_diff = val - min_val
	else:
	  max_diff = max(val - min_val, max_diff)
	prev_val = val

print(max_diff)