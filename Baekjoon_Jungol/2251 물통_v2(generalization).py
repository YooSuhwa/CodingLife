'''
   @ 2019.12.30 ush
   * 백준 알고리즘 - 2251 물통 (https://www.acmicpc.net/problem/2251)
   * python (PyPy3)

   * BFS
   * 2251 물통_v1.py 을 일반화하여 구현

   * 세 물통 A,B,C 중 A,B는 비어있고 C는 가득 차있다.
   * 어떤 물통에 들어있는 물을 다른 물통으로 쏟아 부을 수 있다.
        1. 이때 앞의 물통이 빌때까지 붓거나
        2. 뒤의 물통이 가득 찰 때까지 붓게 된다.
   * A가 비어있을 때, C에 들어갈 수 있는 양을 모두 구하는 문제

'''
from collections import deque

size = list(map(int, input().strip().split(' ')))
sum = size[2]

sideFr = [0, 0, 1, 1, 2, 2]   # from
sideTo = [1, 2, 0, 2, 0, 1]   # to

q = deque()
visit = [[False] * (201) for _ in range(201)]
answer = []

q.append((0,0))
visit[0][0] = True
answer.append(size[2])

abc = [0]*3
next = [0]*3

while q :
    now = q.popleft()

    abc[0] = now[0]
    abc[1] = now[1]
    abc[2] = sum - abc[0] - abc[1]

    for i in range(6):
        #next = abc[:]
        next[0] = abc[0]
        next[1] = abc[1]
        next[2] = abc[2]

        next[sideTo[i]] += next[sideFr[i]]
        next[sideFr[i]] = 0

        if next[sideTo[i]] >= size[sideTo[i]]:
            next[sideFr[i]] = next[sideTo[i]] - size[sideTo[i]]
            next[sideTo[i]] = size[sideTo[i]]

        if not visit [next[0]][next[1]]:
            visit[next[0]][next[1]] = True
            q.append((next[0],next[1]))
            if next[0] == 0 :
                answer.append(next[2])

answer.sort()
for i in answer:
    print(i, end=" ")