for i, a in enumerate(sorted(list(map(lambda a : int(a), input().split(" "))))):
	if i == 0:
		print("%d" % a, end ="")
	else:
		print(" %d"% a, end ="")
print()