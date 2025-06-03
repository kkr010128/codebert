import copy

def solve(h,w,k,stage,nh,nw):
    if nh == h and nw == w:
        res = 0
        for row in stage:
            res += row.count('#')
        if res == k:
            return 1
        else:
            return 0
    
    elif nh == h:
        nwn = nw + 1
        stagen = copy.deepcopy(stage)
        for i in range(h):
            stagen[i][nw] = '.'

        return solve(h,w,k,stage,nh,nwn) + solve(h,w,k,stagen,nh,nwn)
    
    else:
        nhn = nh + 1
        stagen = copy.deepcopy(stage)
        stagen[nh] = list('.'*w)
        return solve(h,w,k,stage,nhn,nw) + solve(h,w,k,stagen,nhn,nw)




if __name__ == '__main__':
    h,w,k = map(int,input().split())
    stage = []
    for i in range(h):
        row = list(input())
        stage.append(row)
    
    print(solve(h,w,k,stage,0,0))
        


