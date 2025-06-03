#coding: UTF-8

buf = input()
word = input()
buf_buf = buf + buf

if word in buf_buf:
    print("Yes")
else:
    print("No")
