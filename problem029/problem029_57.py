
import math

def run():
    x1,y1,x2,y2=tuple(map(float,input().split()))
    
    r=math.sqrt((x1-x2)**2+(y1-y2)**2)
    
    
    print(f"{r:.30f}")


run()
