import sys, itertools
  
for count, input in zip(itertools.count(1), sys.stdin):
    if int(input) == 0: break
    print('Case {0}: {1}'.format(count, input), end='')