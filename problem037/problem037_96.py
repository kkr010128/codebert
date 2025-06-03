minute = int(input())
print('{}:{}:{}'.format(minute // 3600, (minute % 3600) // 60, (minute % 3600) % 60))
