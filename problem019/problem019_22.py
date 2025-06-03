queue,decrease = (int(n) for n in input().split(' '))
targ = []
for q in range(queue):
    targ.append([n for n in input().split(' ')])
length = 0
time = 0
while True:

    if int(targ[length][1]) - decrease <= 0:
        time += int(targ[length][1])
        print(str(targ[length][0]) + " " + str(time))
        targ.pop(length)
        queue -= 1
        if queue == 0:
            break
        length = (length) % queue
        
    else:
        time += decrease
        targ[length][1] = int(targ[length][1]) - decrease
        length = (length + 1) % queue