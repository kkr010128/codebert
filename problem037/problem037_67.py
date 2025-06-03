input = int(input().strip())

hour = input // 3600
min = (input - 3600*hour) // 60
sec = input - 3600 * hour - 60 * min 

print (":".join([str(hour), str(min), str(sec)]))