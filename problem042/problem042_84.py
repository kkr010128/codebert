class itp1_3b:
    def out(self,i,x):
        print "Case "+str(i)+": "+str(x)
if __name__=="__main__":
    run=itp1_3b()
    i=1
    while(True):
        
        x=input()
        if x==0:
            break
        run.out(i,x)
        i+=1