sute = map(int,raw_input().split()) 
num = map(int,raw_input().split())
for i in range(len(num) - 1):
    print "%d" % num[len(num) - i - 1],
print num[0]