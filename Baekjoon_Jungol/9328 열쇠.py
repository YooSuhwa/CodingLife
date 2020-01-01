from collections import deque

h, w = map(int, input().strip().split(' '))
board = ['*.'+input()+'.*' for _ in range(h)]
h += 4
w +=4
board = ['*'*w]+['*'+'.'*(w-2)+'*'] + board + ['*'+'.'*(w-2) + '*'] + ['*'*w]

print(board)