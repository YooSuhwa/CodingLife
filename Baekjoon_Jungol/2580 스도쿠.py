'''
   @ 2019.12.23 ush
   * 백준 알고리즘 - 2580 스도쿠 (https://www.acmicpc.net/problem/2580)
   * python

   * 스도쿠에서 만족해야 할 3가지 조건
   * 1. 각 행에는 0-9가 하나씩 들어가야 한다 << checkRow로 확인
   * 2. 각 열에는 0-9가 하나씩 들어가야 한다 << checkLow로 확인
   * 3. 3*3 사각형에는 0-9가 하나씩 들어가야 한다. << checkSq로 확인

   * 개선해야 할 점 : python 시간초과
'''
def findSq(r, c):
    return (r//3)*3 + (c//3)

def printSudoku():
    for row in sudoku:
        print(' '.join(map(str, row)))
    return 1


def goSudoku(index, N):
    if index == N :
        printSudoku()
        exit(0)

    row = index // n
    col = index % n

    if sudoku[row][col] !=0 :
        goSudoku(index+1, N)

    else :
        for i in range(1, n+1):
            if checkRow[row][i] ==False and checkCol[col][i] == False and checkSq[findSq(row, col)][i] == False:
                sudoku[row][col] = i
                checkRow[row][i] = True
                checkCol[col][i] = True
                checkSq[findSq(row, col)][i] = True

                goSudoku(index+1, N)

                sudoku[row][col] = 0
                checkRow[row][i] = False
                checkCol[col][i] = False
                checkSq[findSq(row, col)][i] = False


n = 9
N = 81
checkRow = [[False]*(n+1) for _ in range(n)]
checkCol = [[False]*(n+1) for _ in range(n)]
checkSq = [[False]*(n+1) for _ in range(n)]

sudoku = [list(map(int,input().split())) for _ in range(n)]


for row in range(0, n):
    for col in range(0, n):
        num = sudoku[row][col]

        if num != 0 :
            checkRow[row][num] =  True
            checkCol[col][num] = True
            checkSq[findSq(row, col)][num] = True

goSudoku(0, N)