class itp1_1d:
    def cal(self,time):
        h=time/3600
        time%=3600
        m=time/60
        time%=60
        s=time
        print str(h)+":"+str(m)+":"+str(s)
if __name__=="__main__":
    time=input()
    run=itp1_1d()
    run.cal(time)