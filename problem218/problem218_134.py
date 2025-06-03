n=int(input())
arr=[input() for _ in range(n)]
dic={}
for i in range(n): #各単語の出現回数を数える
 if arr[i] not in dic:
   dic[arr[i]]=1
 else:
   dic[arr[i]]+=1
largest=max(dic.values()) #最大の出現回数を求める
ans=[]
for keys in dic.keys():
 if dic[keys]==largest: #出現回数が最も多い単語を集計する
   ans.append(keys)
ans=sorted(ans) #単語を辞書順に並べ替えて出力する
for words in ans:
 print(words)