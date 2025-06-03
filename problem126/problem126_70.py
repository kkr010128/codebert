#template
def inputlist(): return [int(j) for j in input().split()]
#template
li = inputlist()
for i in range(5):
    if li[i] == 0:
        print(i+1)