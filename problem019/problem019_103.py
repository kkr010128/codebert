
import Queue
n,q=map(int,raw_input().strip().split())
name=[]
time=[]
qu=Queue.Queue()
class task:
    def __init__(self,name,time):
        self.name=name
        self.time=time
        self.total=0
for i in xrange(n):
    inp=raw_input().strip().split()
    qu.put(task(inp[0],int(inp[1])))
curtime=0

while not qu.empty():
    tmp=qu.get()
    if tmp.time>q:
        tmp.time-=q
        curtime+=q
        qu.put(tmp)
    else:

        curtime+=tmp.time
        ed='' if qu.qsize()==0 else '\n'
        print tmp.name,curtime
#    print curtime



