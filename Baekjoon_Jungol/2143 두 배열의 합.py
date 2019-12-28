'''
   @ 2019.12.28 ush
   * 백준 알고리즘 - 2143 두 배열의 합 (https://www.acmicpc.net/problem/2143)
   * python

   * MITM
   * 두 배열 A,B가 주어졌을 때, A의 부 배열의 합과 B의 부배열의 합을 더한 것이 find가 되는 경우의 수 구하기
    * 부 배열은 A[i], A[i+1], …, A[j-1], A[j] (단, 1 ≤ i ≤ j ≤ n)을 말한다. 
    * 이러한 부 배열의 합은 A[i]+…+A[j]를 의미한다. 즉 배열의 연속된 합
   * 1. a,b 배열에 대한 모든 부배열의 합을 계산하여 team1, team2에 저장
   * 2. a의 각 부배열 합에 대해서 'find-a ==b'인 b의 부분합의 개수를 센다.
'''
from collections import Counter

find = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

team1 = []
team2 = []

#부 배열은 연속된거!!!!! 따라서 bit마스크 안썼음
for i in range(n):
    temp = 0
    for j in range(i, n):
        temp += a[j]
        team1.append(temp)

for i in range(m):
    temp = 0
    for j in range(i, m):
        temp += b[j]
        team2.append(temp)

team1.sort()
team2.sort()

counter = Counter(team2)

answer = 0
for num in team1:
    temp = find - num
    answer += counter[temp]

print(answer)