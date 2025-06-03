
splited = input().split(" ")
f = int(splited[0])/int(splited[1])
r = int(splited[0])%int(splited[1])
d = int(splited[0])//int(splited[1])
print(d, r, "{0:.5f}".format(f))