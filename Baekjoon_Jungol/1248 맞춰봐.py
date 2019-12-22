'''
   @ 2019.12.22 ush
   * 백준 알고리즘 - 1248 맞춰봐 (https://www.acmicpc.net/problem/1248)
   * python (PyPy3)

   * backtracking

   * Smatrix[i][j] = A[i]+A[i+1]+...+A[j] 의 부호
   * Smatrix[i][i] = A[i]의 부호 #즉, A[i]의 부호 그 자체
   * 1. 입력S를 통해 Smatrix를 만든다
   * 2. 재귀함수 go 호출
   * 3. go 함수 안에서, Smatrix[i][i]가 A[i]의 부호임을 이용하여 -10~10의 값을 answer에 차례로 넣는다
   * 4. check함수를 통해 answer[index]의 값이 Smatrix에 부합하는지 확인한다.
   * 5. index == N일때까지 재귀함수 go를 실행하여 answer을 얻는다.

'''
def check(index):
    sum = 0
    for i in range(index, -1, -1):
        sum += answer[i]
        if Smatrix[i][index] == 0 and sum != 0:
            return False
        if Smatrix[i][index] > 0 and sum <= 0:
            return False
        if Smatrix[i][index] < 0 and sum >= 0 :
            return False

    return True

def go(index):
    if index == N :
        return True
    if Smatrix[index][index] == 0:
        answer[index] = 0
        return check(index) and go(index+1)

    for i in range(1,11):
        answer[index] = Smatrix[index][index] * i
        if check(index) and go(index+1) :
            return True
    return False

N = int(input())
S = input()
Smatrix = [[0]*N for _ in range(N)]
answer = [0]*N
count = 0
for i in range(0, N):
    for j in range(i, N):
        if S[count] == '-':
            Smatrix[i][j] = -1
        elif S[count] == '+' :
            Smatrix[i][j] = 1
        else: #0
            Smatrix[i][j] = 0
        count +=1

go(0)
print(' '.join(map(str,answer)))