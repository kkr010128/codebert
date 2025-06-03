S = input()
if len(S) >= 1 and len(S) <= 1000:
	if S[-1] == "s":
  		print (S, "es", sep = '')
	else:
  		print (S, "s", sep = '')