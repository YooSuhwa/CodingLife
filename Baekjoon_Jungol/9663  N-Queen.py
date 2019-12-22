'''
   @ 2019.12.22 ush
   * 백준 알고리즘 - 9663 N-Queen (https://www.acmicpc.net/problem/9663)
   * python (PyPy3)

   * backtracking
   * Queen은 가로, 세로, 대각선 모두 공격 할 수 있음. 따라서 한 row, col, 오른쪽 위 대각선, 왼쪽 위 대각선 모두 체크해줘야 한다
   * 1. goRow : 각 row당 하나의 Q만 있도록 재귀함수를 실행
   * 2. checkOver : 같은 col당 하나의 Q만 있도록
   * 3. checkDiagR : 오른쪽 위 대각선에 하나의 Q만 있도록
   * 4. checkDiagL : 왼쪽 위 대각선에 하나의 Q만 있도록

   *
'''
def check (row, col, N):
    if checkOver[col] == 1:
        return -1
    if checkDiagR[row+col] == 1 :
        return -1
    if checkDiagL[row-col+N -1] == 1:
        return -1
    return 1

def goRow(row, N):
    if row == N :
        return 1

    answer = 0
    for col in range(0, N):
        if check(row, col, N) == 1:
            checkOver[col] = 1
            checkDiagR[row+col] = 1
            checkDiagL[row-col+N-1] = 1

            answer+= goRow(row + 1, N)

            checkOver[col] = 0
            checkDiagR[row + col] = 0
            checkDiagL[row - col + N - 1] = 0
    return answer

n = int(input())
checkOver = [0] * n
checkDiagR = [0] * (2*n-1)
checkDiagL = [0] * (2*n-1)

print(goRow(0, n))
