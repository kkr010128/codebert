# -*- coding: utf-8 -*-

sen = ''
while True:
    try:
        buf = raw_input()
    except:
        break
    sen += buf.lower()
for i in range(ord('a'), ord('z')+1):
    print "%s : %d" %(chr(i), sen.count(chr(i)))