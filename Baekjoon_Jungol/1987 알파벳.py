'''
   @ 2019.12.23 ush
   * 백준 알고리즘 - 1987 알파벳 (https://www.acmicpc.net/problem/1987)
   * python (PyPy3)

   * 1. 상하좌우로 가는 newx, newy가 가능한 값인지 체크한다
   * 2. 만약 newx, newy가 가능한 값이라면 visit을 통해 이미 방문한 알파벳인지 확인한다
   
'''
def go(x, y, count, visit):
    global answer
    if count > answer:
        answer = count

    for k in range(0, 4):
        newx = x + dx[k]
        newy = y + dy[k]

        if newx >-1 and newx < r and newy > -1 and newy <c :
            ch = ord(board[newx][newy]) - ord('A')

            if visit[ch] == False :
                visit[ch] = True
                go(newx, newy, count+1, visit)
                visit[ch] = False

r, c = map(int, input().strip().split(' '))
board = [input() for _ in range(r)]
visitAlpha = [False]*27

dx = [0,0,1,-1]
dy = [1,-1,0,0]

ch = ord(board[0][0]) - ord('A')
visitAlpha[ch] = True

answer = 0

go(0, 0, 1,  visitAlpha)
print(answer)