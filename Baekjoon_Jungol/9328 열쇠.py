from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

h, w = map(int, input().strip().split(' '))

board = ['*.'+input()+'.*' for _ in range(h)]
key = set(input())
h += 4
w +=4
board = ['*'*w]+['*'+'.'*(w-2)+'*'] + board + ['*'+'.'*(w-2) + '*'] + ['*'*w]

q = deque()
q_alpha = [deque() for _ in range(26)] #알파벳 별 큐
visit = [[False]*w for _ in range(h)]

q.append((1,1))
visit[1][1]= True

answer = 0
while q:
    now = q.popleft()
    x = now[0]
    y = now[1]

    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]

        if visit[newX][newY] :
            continue

        visit[newX][newY] = True

        pos = board[newX][newY]
        if pos == '*' : #벽
            continue
        elif pos == '$' : #문서
            answer += 1
            q.append((newX, newY))
        elif 'A' <= pos <= 'Z': #문 대문자
            if pos in key : #이미 키 있는 문
                q.append((newX, newY))
            else : #키 없는 문
                q_alpha[ord(pos)-ord('A')].append((newX, newY))
        elif 'a' <= pos <= 'z' : #열쇠 소문자
            q.append((newX, newY))
            if pos not in key : #처음본 열쇠
                temp = ord(pos)-ord('A')
                while q_alpha[temp]:
                    q.append(q_alpha[temp].popleft())

print(answer)


