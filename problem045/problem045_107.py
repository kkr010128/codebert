
splited = input().split(" ")
f = int(splited[0])/int(splited[1])
r = int(splited[0])%int(splited[1])
d = int(splited[0])//int(splited[1])
print('%s %s %.5f' % (d, r, f))