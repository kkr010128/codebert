
string = list(raw_input())
q = input()
List = [0]*q
for i in range(q):
	List[i] = raw_input().split()
	List[i][1:3] = map(int,List[i][1:3])
	if List[i][0] == 'print' :
		print '%s' %"".join(string[List[i][1]:List[i][2]+1])
	elif List[i][0] == 'reverse':
		s = [0] * (List[i][2]-List[i][1])
		s = reversed(string[List[i][1]:List[i][2]+1])
		string[List[i][1]:List[i][2]+1] = s
	else :
		string[List[i][1]:List[i][2]+1] = list(List[i][3])