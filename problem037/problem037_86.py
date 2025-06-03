# coding: utf-8
 
uSec = 1
uMinute = 60 * uSec
uHour = 60 * uMinute
 
input_secs = int(raw_input().rstrip())
 
h = input_secs / uHour
m = (input_secs - h * uHour) / uMinute
s = (input_secs - h * uHour - m * uMinute) / uSec
 
print ':'.join([str(x) for x in [h, m, s]])