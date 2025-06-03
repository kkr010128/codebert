import heapq
X,Y,A,B,C = map(int,input().split())

qa = list(map(int,input().split()))
qb = list(map(int,input().split()))
r = list(map(int,input().split()))

qa.sort(reverse=True)
qb.sort(reverse=True)
r.sort(reverse=True)

qa_ans = qa[:X]
qb_ans = qb[:Y]

heapq.heapify(qa_ans)
heapq.heapify(qb_ans)

for i in range(C):
    r_max = r[i]

    qa_min = heapq.heappop(qa_ans)
    qb_min = heapq.heappop(qb_ans)

    if (r_max>qa_min) or (r_max>qb_min):
        if qa_min >qb_min:
            heapq.heappush(qa_ans,qa_min)
            heapq.heappush(qb_ans,r_max)
        else:
            heapq.heappush(qa_ans,r_max)
            heapq.heappush(qb_ans,qb_min)

    else:
        heapq.heappush(qa_ans, qa_min)
        heapq.heappush(qb_ans, qb_min)
        break

print(sum(qa_ans)+sum(qb_ans))