def resolve():
	s, w = map(int, input().split())
	if s <= w:
		print("unsafe")
	else:
		print("safe")

resolve()
