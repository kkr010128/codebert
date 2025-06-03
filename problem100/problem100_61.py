x=int(input())
if x in range(400,600):
    p=8
elif x in range(600,800):
    p=7
elif x in range(800,1000):
    p=6
elif x in range(1000,1200):
    p=5
elif x in range(1200,1400):
    p=4
elif x in range(1400,1600):
    p=3
elif x in range(1600,1800):
    p=2
elif x in range(1800,2000):
    p=1
print(p)