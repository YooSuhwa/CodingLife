'''
   @ 2020.01.01 ush
   * 백준 알고리즘 - 9328 열쇠 (https://www.acmicpc.net/problem/9328)
   * python

   * BFS

   * 훔칠 수 있는 문서의 최대 개수를 구하는 문제
   * 큐를 총 27개 이용.
   	* 일반적인 BFS 큐(q) 1개 / 대문자 알파벳 별 큐 26개 (열쇠가 없는 문을 만나면 해당 알파벳 큐에 좌표 추가)
   * 1. 문제에서 '빌딩의 밖으로 나갈 수 있다'고 하였으므로 전체 board를 '*.' 으로 감싼다.
   * 2. board가 확장되었으므로 (0,0)이 아닌 (1,1)에서 시작한다.
   * 3. dx, dy (상하좌우)에 대해서
   		* a) visit == False	인지 확인
   		* b) board 가 벽(*)	인지 확인
   		* c) board 가 문서($)	인지 확인 >> answer++ and q.push
   		* d) board 가 문(대문자 알파벳)인지 확인
   			* 이미 열쇠를 가지고 있는 문이라면 >> q.push
   			* 열쇠가 없는 문이라면 해당 알파벳의 큐에 넣음 (q_alpha(해당문).push)
   		* e) board 가 열쇠(소문자 알파벳)인지 확인
   			* 해당 열쇠가 처음 본 열쇠라면 
   				>> key에 넣기 and q_alpha에 있던 모든 좌표를 q에 넣는다
   * 4. answer 출력
'''

from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

testCase = int(input())
for _ in range(testCase):
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

            pos = board[newX][newY]
            if pos == '*' : #벽
                continue

            visit[newX][newY] = True
            if pos == '.' :
                q.append((newX, newY))
            elif pos == '$' : #문서
                answer += 1
                q.append((newX, newY))
            elif 'A' <= pos <= 'Z': #문 대문자
                if pos.lower() in key : #이미 키 있는 문
                    q.append((newX, newY))
                else : #키 없는 문
                    q_alpha[ord(pos)-ord('A')].append((newX, newY))
            elif 'a' <= pos <= 'z' : #열쇠 소문자
                q.append((newX, newY))
                if not pos in key : #처음본 열쇠
                    key.add(pos)
                    temp = ord(pos)-ord('a')
                    #print(temp)
                    while q_alpha[temp]:
                        q.append(q_alpha[temp].popleft())

    print(answer)


