while True:
    try:
        a = map(int,raw_input().split())

	n = [a[0],a[1]]

        while True:
            if a[0] < a[1]:
	        tmp = a[0]
                a[0] = a[1]
	        a[1] = tmp

            a[0] = a[0] - a[1]
	    if a[0] == 0:
		break

	b = n[0]*n[1]/a[1]

	print "%d %d" % (a[1],b)

    except EOFError:
	break