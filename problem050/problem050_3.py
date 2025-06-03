while True:
	h,w = [int(s) for s in input().split(' ')]
	if h==0 and w==0:
		break
	else:
		top_bottom = '#'*w + '\n'
		low = '#' + '.'*(w-2) + '#\n'
		rectangle = top_bottom + low*(h-2) + top_bottom
		print(rectangle)