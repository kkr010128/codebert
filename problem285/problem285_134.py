import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(IN())
mod=1000000007

#+++++

def main():
	#a = int(input())
	#b , c = tin()
	s = input()
	if s[0] == '>':
		s = '<' + s
		
	if s[-1] == '<':
		s = s + '>_'
	else:
		s = s + '_'
		
	dd = []
	pre = '<'
	count = [1,0]
	for c in s[1:]:
		if c == '<' and pre == '<':
			count[0] += 1
		elif c == '>' and pre == '>':
			count[1] += 1
		elif c == '>' and pre == '<':
			pre = '>'
			count[1] = 1
		elif c == '<' and pre == '>':
			pre = '<'
			dd.append(count)
			count=[1,0]
		else:
			dd.append(count)
	
	ret_sum = 0
	for l, r in dd:
		ret_sum += (r*(r+1)//2) + (l*(l+1)//2) - min(r,l)
	print(ret_sum)
		
		
	
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)
		
def input_clipboard():
	import clipboard
	input_text=clipboard.get()
	input_l=input_text.splitlines()
	for l in input_l:
		yield l

if __name__ == "__main__":
	if sys.platform =='ios':
		if input_method==input_methods[0]:
			ic=input_clipboard()
			input = lambda : ic.__next__()
		elif input_method==input_methods[1]:
			sys.stdin=open('inputFile.txt')
		else:
			pass
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)