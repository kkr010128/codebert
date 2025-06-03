# -encoding:utf-8
class itp1_1c:
    def cal(self,a,b):
        self.a=a
        self.b=b
        print str(a*b)+" "+str(2*a+2*b)
        
if __name__=="__main__":
    ip=map(int,raw_input().split(" "))
    run=itp1_1c()
    run.cal(ip[0],ip[1])