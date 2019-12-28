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
from collections import Counter

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

''' 시간초과 
for num in teamAB:
    answer += teamCD.count(-num)
'''

counter = Counter(teamCD)
#Counter({40: 2, 26: 1, 72: 1, 119: 1, -4: 1, 104: 1, 87: 1, 86: 1, 133: 1, 10: 1, 118: 1, 101: 1, -53: 1, -7: 1, -83: 1, 25: 1, 8: 1, -91: 1, -45: 1, 2: 1, -121: 1, -13: 1, -30: 1, -26: 1, 20: 1, 67: 1, -56: 1, 52: 1, 35: 1, -22: 1, 24: 1, 71: 1, -52: 1, 56: 1, 39: 1})
print(counter)
for num in teamAB:
    answer += counter[-num]

print(answer)