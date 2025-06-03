sec_input = int(input())
hour = sec_input // (60 * 60)
remain = sec_input % (60 * 60)
min = remain // 60
sec = remain % 60

print('%d:%d:%d' % (hour, min, sec))