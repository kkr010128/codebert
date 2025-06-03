#coding:UTF-8
def Rec(N,List):
    for i in range(N):
        a=int(List[i].split(" ")[0])
        b=int(List[i].split(" ")[1])
        c=int(List[i].split(" ")[2])
        if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
            print("YES")
        else:
            print("NO")

if __name__=="__main__":
    List=[]
    N=int(input())
    for i in range(N):
        List.append(input())
    Rec(N,List)