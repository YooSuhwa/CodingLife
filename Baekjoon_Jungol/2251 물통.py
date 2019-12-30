'''
   @ 2019.12.30 ush
   * 백준 알고리즘 - 2251 물통 (https://www.acmicpc.net/problem/2251)
   * python (PyPy3)

   * BFS

   * 세 물통 A,B,C 중 A,B는 비어있고 C는 가득 차있다.
   * 어떤 물통에 들어있는 물을 다른 물통으로 쏟아 부을 수 있다.
        1. 이때 앞의 물통이 빌때까지 붓거나
        2. 뒤의 물통이 가득 찰 때까지 붓게 된다.
   * A가 비어있을 때, C에 들어갈 수 있는 양을 모두 구하는 문제

'''

from collections import deque

aSize, bSize, cSize = map(int, input().strip().split(' '))
sum = cSize

q = deque()
visit = [[False] * (201) for _ in range(201)]
answer = []

q.append((0,0))
visit[0][0] = True
answer.append(cSize)

while q :
    now = q.popleft()
    a = now[0]
    b = now[1]
    c = sum - a - b

    # 1. a >> b
    newA = a
    newB = b
    newC = c

    newB += newA
    newA = 0

    if newB >= bSize:
        newA = newB - bSize
        newB = bSize

    if not visit[newA][newB]:
        visit[newA][newB] = True
        q.append((newA, newB))
        if newA == 0 :
            answer.append(newC)

    # 2. a >> c
    newA = a
    newB = b
    newC = c

    newC += newA
    newA = 0

    if newC >= cSize:
        newA = newC - cSize
        newC = cSize

    if not visit[newA][newB]:
        visit[newA][newB] = True
        q.append((newA, newB))
        if newA == 0:
            answer.append(newC)

    #3. b >> a
    newA = a
    newB = b
    newC = c

    newA += newB
    newB = 0

    if newA >= aSize:
        newB = newA - aSize
        newA = aSize

    if not visit[newA][newB]:
        visit[newA][newB] = True
        q.append((newA, newB))
        if newA == 0:
            answer.append(newC)

    #4. b >> c
    newA = a
    newB = b
    newC = c

    newC += newB
    newB = 0

    if newC >= cSize:
        newB = newC - cSize
        newC = cSize

    if not visit[newA][newB]:
        visit[newA][newB] = True
        q.append((newA, newB))
        if newA == 0:
            answer.append(newC)

    #5. c >> a
    newA = a
    newB = b
    newC = c

    newA += newC
    newC = 0

    if newA >= aSize:
        newC = newA - aSize
        newA = aSize

    if not visit[newA][newB]:
        visit[newA][newB] = True
        q.append((newA, newB))
        if newA == 0:
            answer.append(newC)

    #6. c >> b
    newA = a
    newB = b
    newC = c

    newB += newC
    newC = 0

    if newB >= bSize:
        newC = newB - bSize
        newB = bSize

    if not visit[newA][newB]:
        visit[newA][newB] = True
        q.append((newA, newB))
        if newA == 0:
            answer.append(newC)


answer.sort()
for i in answer:
    print(i, end=" ")