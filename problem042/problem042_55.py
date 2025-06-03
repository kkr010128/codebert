import sys
  
l = sys.stdin.readlines()

for i in range(len(l)-1):
    print('Case {}: {}'.format(i+1,l[i].strip()))
