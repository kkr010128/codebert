s = input()
start, count, end = 0, 0, len(s)-1
while(start < end):
    if (s[start] != s[end]):
        count += 1
        start += 1; end -= 1
    else:
        start += 1; end -= 1
else:
    print(count)