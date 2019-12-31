'''
   @ 2019.12.31 ush
   * 백준 알고리즘 - 2251 물통 (https://www.acmicpc.net/problem/2251)
   * python (PyPy3)

   * BFS
   * 2251 물통_v1.py 을 일반화하여 구현
   * 2251 물통_v1.py 를 더 알아보기 쉽게 구현 
   * 알고리즘은 동일

   * 세 물통 A,B,C 중 A,B는 비어있고 C는 가득 차있다.
   * 어떤 물통에 들어있는 물을 다른 물통으로 쏟아 부을 수 있다.
        1. 이때 앞의 물통이 빌때까지 붓거나
        2. 뒤의 물통이 가득 찰 때까지 붓게 된다.
   * A가 비어있을 때, C에 들어갈 수 있는 양을 모두 구하는 문제
'''
from collections import deque

size = list(map(int, input().strip().split(' ')))
sum = size[2]

side = list(zip([0,0,1,1,2,2], [1,2,0,2,0,1]))

q = deque()
visit = [[False] * (201) for _ in range(201)]
answer = []

q.append((0,0))
visit[0][0] = True
answer.append(size[2])

while q :
    now = q.popleft()

    abc = [now[0], now[1], (sum-now[0]-now[1])]

    for fr, to in side:
        next = abc[:]

        next[to] += next[fr]
        next[fr] = 0

        if next[to] >= size[to]:
            next[fr] = next[to] - size[to]
            next[to] = size[to]

        if not visit [next[0]][next[1]]:
            visit[next[0]][next[1]] = True
            q.append((next[0],next[1]))
            if next[0] == 0 :
                answer.append(next[2])

answer.sort()
for i in answer:
    print(i, end=" ")
