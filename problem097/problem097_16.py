K = int(input())
verbose = False

path = set()
a = 0
step = 0
while True:
    step += 1
    a = (a*10 + 7) % K
    if verbose: print (step, ':', a)
    if a == 0:
        print (step)
        break
    if a in path:
        print ('-1')
        break
    path.add(a)
