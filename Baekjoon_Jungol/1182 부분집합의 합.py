'''
   @ ush 2019/12/28
   * 백준 알고리즘 - 1182 부분수열의 합 (https://www.acmicpc.net/problem/1182)
   * python

   * 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 find가 되는 경우의 수를 구하기
   * bitmask를 이용하여 모든 부분 수열의 합을 구한다
'''
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