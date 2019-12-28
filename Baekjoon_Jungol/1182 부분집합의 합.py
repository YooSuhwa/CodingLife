n,find = map(int,input().split())
arr = list(map(int,input().split()))
totalSet = [0]*(1<<n)

for i in range(1<<n) :
    for k in range(n):
        if i&(1<<k) :
            totalSet[i] += arr[k]

answer = totalSet.count(find)
if find == 0 :
    answer-=1
print(answer)