input = int(raw_input())
h = input / 3600
input -= h * 3600
m = input / 60
input -= m * 60
print str(h) + ":" + str(m) + ":" + str(input)