in_sec = int(raw_input())
sec = in_sec%60
in_sec = (in_sec-sec)/60
min = in_sec%60
h = (in_sec-min)/60
print str(h) + ":" + str(min) + ":" + str(sec)