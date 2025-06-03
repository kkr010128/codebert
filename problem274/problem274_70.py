import sys

#+++++

def main():
	n, m = map(int, input().split())
	s=input()
	s=s[::-1]
	#arch=[len(s)+100]*len(s)
	
	pos=0
	ret=[]
	while pos < len(s)-1:
		for mi in range(m,0,-1):
			if pos+mi >= len(s):
				pass
			elif s[pos+mi]=='0':
				pos += mi
				ret.append(mi)
				#print(pos)
				break
			else:
				pass
		else:
			return -1
	
	r=ret[::-1]
	print(*r)
	
'''
def main2():
	n, m = map(int, input().split())
	s = input()
	
	tt=[-1]*len(s)
	t_parent=[-1]*len(s)
	rs=s[::-1]
	open_list=[0]
	max_dist = 0
　	while True#len(open_list) > 0:
		st, parent, count = open_list.pop()
		for i in range(m, 0, -1):
			aa = st + i
			if aa > n+1:
				pass
			
			#gmマス
			if rs[aa] == 1:
				continue
			
			#アクセス済み
			if tt[aa] > 0:
				break
				
			tt[aa] = count+1
			t_parent[aa] = st
			open_list.append(aa, st, count+1)
			
	print(1)
'''
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)

if __name__ == "__main__":
	if sys.platform =='ios':
		sys.stdin=open('inputFile.txt')
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)