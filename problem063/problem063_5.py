count = {}
for i in range(26):
    count[(i)] = 0

while True:
    try:
        x = raw_input()
    except:
        break
    for i in range(len(x)):
        if(ord('a') <= ord(x[i]) and ord(x[i]) <= ord('z')):
            count[(ord(x[i])-ord('a'))] += 1
        elif(ord('A') <= ord(x[i]) and ord(x[i]) <= ord('Z')):
            count[(ord(x[i])-ord('A'))] += 1

for i in range(26):
    print '%s : %d' %(chr(i+ord('a')), count[(i)])
exit(0)