import sys

counter = {k: 0 for k in  "abcdefghijklmnopqrstuvwxyz"}

while True:
    try:
        line = raw_input()
    except:
        break
    for i in line.lower():
        if i in counter.keys():
            counter[i] += 1
for k in sorted(counter.keys()):
    print "{} : {}".format(k,counter[k])