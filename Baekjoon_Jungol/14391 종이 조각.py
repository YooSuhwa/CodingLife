'''
   @ 2019.12.24 ush
   * 백준 알고리즘 - 14391 종이 조각 (https://www.acmicpc.net/problem/14391)
   * python

   * bit mask

   * 종이를 조각으로 잘라서 합의 최대값 구하기
   * 각 칸은 가로 혹은 세로로 나눠진다.
   * 따라서 비트 마스크로 풀이가 가능하다.

'''
n, m = map(int,input().split())
paper = [list(map(int,list(input()))) for _ in range(n)]

answer = 0
final = n*m

#가로 0, 세로 1
sum = 0
for seq in range(0, 1<<(final)):
    sum = 0
    #가로 0
    temp = 0
    for row in range(0, n):
        for col in range(0, m):
            k = row * m + col
            if seq&(1<<k) == 0 :
                temp = (temp *10 + paper[row][col])
            else :
                sum += temp
                temp = 0
        sum += temp
        temp = 0

    #세로 1
    temp = 0
    for col in range(0, m):
        for row in range(0, n) :
            k = row * m + col
            if seq&(1<<k) != 0 :
                temp = (temp*10 + paper[row][col])
            else:
                sum += temp
                temp = 0
        sum += temp
        temp = 0

    answer = max(answer, sum)
    
print(answer)