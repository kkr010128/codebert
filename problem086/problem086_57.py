total, max, time=map(int, input().split())

print (time*int(total/max) if total%max==0 else time*(int(total/max)+1))
