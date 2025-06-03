watch = int(input())

hour= watch//3600

watch -= hour *3600

minute = watch // 60

watch -=minute*60

print(hour,minute,watch,sep=':')

