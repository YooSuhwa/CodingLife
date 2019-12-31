from collections import deque

size = list(map(int, input().strip().split(' ')))
sum = size[2]

sideFr = [0, 0, 1, 1, 2, 2]
sideTo = [1, 2, 0, 2, 0, 1]

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
        #next = abc
        next[0] = abc[0]
        next[1] = abc[1]
        next[2] = abc[2]
        print(next)

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
