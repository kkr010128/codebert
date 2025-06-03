import sys

while True:
    n = sys.stdin.readline()[:-1]

    if n == '-1 -1 -1':
        break

    marks = [ int(m) for m in n.split() ]

    mt_points,retest = marks[0] + marks[1],marks[2]

    if -1 in marks[:-1]:
        print('F')
        continue
    elif mt_points >= 80:
        print('A')
        continue
    elif mt_points >= 65 and 80 > mt_points:
        print('B')
        continue
    elif mt_points >= 50 and 65 > mt_points:
        print('C')
        continue
    elif mt_points >= 30 and 50 > mt_points:
        if retest >= 50:
            print('C')
            continue
        print('D')
        continue
    elif 30 > mt_points:
        print('F')

