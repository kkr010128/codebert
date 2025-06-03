n = int(raw_input())
a = map(int, raw_input().split())

print '{0} {1} {2}'.format(min(a), max(a), sum(a))