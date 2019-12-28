'''
   @ 2019.12.28 ush
   * 백준 알고리즘 - 7453 부등호 (https://www.acmicpc.net/problem/7453)
   * python (PyPy3)

   * A[a]+B[b]+C[c]+D[d] == 0 인 (a,b,c,d) 쌍의 개수 구하기
   * 이때 N의 범위가 1~4,000로 매우 큼. O(N^4)
   * 따라서 A[a]+B[b] == - (C[c]+D[d])로 나누어서 N^2씩 2번 계산하기 
   * MITM

'''

import sys
n = int(input())
temp = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
a,b,c,d = zip(*temp)

teamAB = []
teamCD = []
answer = 0


for i in range(n):
    for j in range(n):
        teamAB.append(a[i]+b[j])
        teamCD.append(c[i]+d[j])

for num in teamAB:
    answer += teamCD.count(-num)

print(answer)