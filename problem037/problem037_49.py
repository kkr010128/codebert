sec_in = int(input())

hour = sec_in // 3600
minute = (sec_in % 3600) // 60
sec = sec_in % 60

print('{0}:{1}:{2}'.format(hour,minute,sec))
