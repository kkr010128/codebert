a=int(input())
hours=a//3600
minutes_num=a%3600
minutes=minutes_num//60
seconds=a%60
print(str(hours)+":"+str(minutes)+":"+str(seconds))

