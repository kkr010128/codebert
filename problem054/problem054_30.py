n = input()
data = []
space = []
for i in ['S ', 'H ', 'C ', 'D ']:
    for j in map( str , xrange(1, 14)):
        data.append(i + j)   
for i in xrange(n):
    data.remove(raw_input())
for i in xrange(len(data)):
    print data[i]