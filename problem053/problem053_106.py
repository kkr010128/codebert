a = input ()
numbers = map(int,raw_input().split())
numbers.reverse()
print ' '.join(map(str,numbers))