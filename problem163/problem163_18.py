ARGS=input().split()
S=int(ARGS[0])
W=int(ARGS[1])

if S > W:
    print('safe')
else:
    print('unsafe')