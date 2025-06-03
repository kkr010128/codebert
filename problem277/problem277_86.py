import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
LIN=lambda : list(IN())
mod=1000000007

#+++++

def main():
	#a = int(input())
	h,w,k = IN()
	ss=0
	ret=[]
	kv=1
	for i in range(h):
		wd = input()
		if ss >= 0 and wd == '.'*w:
			ss+=1
		elif wd == '.'*w:
			al=ret[-1][:]
			ret.append(al)
		else:
			al=[]
			stf=True
			for c in wd:
				if stf and c == '#':
					stf = False
				elif c == '#':
					kv+=1
				al.append(kv)
			else:
				kv+=1
			if ss >= 0:
				for i in range(ss+1):
					ret.append(al)
				ss=-1
			else:
				ret.append(al)
	for l in ret:
		print(*l)
		
		
		
	
	
	
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