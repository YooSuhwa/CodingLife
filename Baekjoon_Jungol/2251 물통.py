from collections import deque

aSize, bSize, cSize = map(int, input().strip().split(' '))
sum = cSize

q = deque()
visit = [[False] * (200) for _ in range(200)]
answer = []

q.append((0,1))
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

    if newB > bSize:
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

    if newC > cSize:
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

    if newA > aSize:
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

    if newC > cSize:
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

    if newA > aSize:
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

    if newB > aSize:
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