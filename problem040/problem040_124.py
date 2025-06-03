a,b,c = map(int, raw_input().split())
value = [a,b,c]
value.sort()
value_str = map(str, value)
print " ".join(value_str)