# coding: utf-8
while True :
	line = list( map(int, input().split(' ')))

	line.sort()

	if(line[0] == 0 and line[1] == 0) :
		break;
	print('{0} {1}'.format(line[0], line[1]))