'''
   @ 2020/01/09 ush
   * 백준 알고리즘 - 11048 이동하기 (https://www.acmicpc.net/problem/11048)
   * python

   * dp

   * 가장 왼쪽 위 칸에서 가장 오른 쪽 아래 칸으로 규칙에 맞게 이동할 수 있는 경로의 수를 구하는 문제
   * 각 칸에 적혀있는 수는 현재 칸에서 갈 수 있는 거리를 의미 
   * 반드시 오른쪽이나 아래쪽으로만 이동 가능함

   * dp[i][j] = (i,j)칸에 갈 수 있는 경로의 개수 일때
    (i,j)칸에 '올 수 있는 칸'을 찾는다
    * (i, j) << (i, k+map[i][k]) #왼쪽에서 옴
    * (i, j) << (k+map[k][j], j) #위에서 옴
'''
n = int(input())
map = [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for i in range(0, n):
    for j in range(0, n):
        if i == 0 and j == 0 :
            dp[i][j] = 1
            continue
        for k in range(0, j):
            if k + map[i][k] == j :
                dp[i][j]+= dp[i][k]
        for k in range(0, i):
            if k + map[k][j] == i:
                dp[i][j] += dp[k][j]


print(dp[n-1][n-1])