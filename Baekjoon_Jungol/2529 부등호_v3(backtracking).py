'''
   @ 2019.12.22 ush
   * 백준 알고리즘 - 2529 부등호 (https://www.acmicpc.net/problem/2529)
   * python

   * backtracking
'''
answer = []

def check(pre, now, inequality):
    if inequality == '<' and int(pre)>int(now):
        return -1
    if inequality == '>' and int(pre)<int(now):
        return -1

    return 1


def go(index, number, visit, inequality, N):
    if index == N :
        answer.append(''.join(number))
        return 0

    for i in range(0, 10):

        if visit[i] : continue
        if index == 0 or (check(number[index - 1], str(i),  inequality[index - 1]) == 1 ):
            visit[i] = 1
            number.append(str(i))
            go(index+1, number, visit, inequality, N)
            visit[i] = 0
            number.remove(str(i))


#main
inequality = []
k = int(input())
inequality = list(input().split())
number = []
visit = [0 for _ in range(0, 10) ]

go(0, number, visit, inequality, k+1)
print(max(answer))
print(min(answer))
