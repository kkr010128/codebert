#coding:utf-8
#1_8_C 2015.4.8
sentence = ''
while True:
    try:
        sentence += input().lower()
    except:
        break

for i in range(ord('a') , ord('z') + 1):
    print('{} : {}'.format(chr(i),sentence.count(chr(i))))