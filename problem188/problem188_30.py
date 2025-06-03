#heapq p,qの最小値側にrの最大値入れていく。
#p_changeとq_changeが等しい場合がおかしかったのを直した
import heapq 

#初期入力
X,Y,A,B,C = (int(x) for x in input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))


# ソート⇒無色と比較
p.sort()
q.sort()
r.sort(reverse=True)

ans_sum =sum(p[-X:]) + sum(q[-Y:])
p_hq = p[-X:]
q_hq = q[-Y:]
heapq.heapify(p_hq)
heapq.heapify(q_hq)
p_change =heapq.heappop(p_hq)
q_change =heapq.heappop(q_hq)
count_p =0
count_q =0
for i in r: #rは大きい順
    if i < p_change and i < q_change:
        break
    if p_change <= q_change:
        if  count_p < X:
            heapq.heappush(p_hq,i)
            count_p +=1
            ans_sum = ans_sum -p_change +i
            p_change =heapq.heappop(p_hq)
    elif p_change > q_change:
        if  count_q < Y:
            heapq.heappush(q_hq,i)
            count_q +=1
            ans_sum = ans_sum -q_change +i
            q_change =heapq.heappop(q_hq)
print(ans_sum)