import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
from collections import Counter
def main():
    n = int(input())
    d1 = {'AC':0, 'WA':0, 'TLE': 0,'RE':0}
    s = []
    for _ in range(n):
        s.append(input())
    sa = Counter(s)
    for k, v in sa.items():
        d1[k] += v
    print('AC x', d1['AC'])
    print('WA x', d1['WA'])
    print('TLE x', d1['TLE'])
    print('RE x', d1['RE'])

if __name__ == '__main__':
    main()
