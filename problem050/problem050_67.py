while True:
	h,w=map(int,input().split())
	if h==w==0:break
	for hh in range(h):
		ol=''
		for ww in range(w):
			if hh == 0 or ww == 0 or hh == h - 1 or ww == w - 1:
				ol+='#'
			else:
				ol+='.'
		print(ol)
	print()