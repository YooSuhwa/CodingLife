'''
   @ ush 2020/01/08
   * 백준 알고리즘 - 11048 이동하기 (https://www.acmicpc.net/problem/11048)
   * python

   * dp

   * (1,1) 에서 (n,m)으로 이동하려고 한다. 
   * 이동할 수 있는 방향은 오른쪽(i,j+1), 왼쪽(i+1, j), 오른쪽아래 대각선(i+1, j+1)이다.
   * map의 각 칸에 사탕이 주어져 있을 때, 가져올 수 있는 사탕 개수의 최댓값을 구하는 프로그램

   * v1) 현재칸으로 올 수 있는 경우의 수를 살펴보기.
   	* 즉, 현재칸을 기준으로 전 단계가 될 수 있는 칸들을 계산하기
'''

def max3(n1, n2, n3):
    return max(max(n1, n2), n3)

n, m = map(int, input().strip().split(' '))
m += 1
map = [[0]+list(map(int,input().split())) for _ in range(n)]
map = [[0]*m] + map
n += 1
dp = [[0]*m for _ in range(n)]
for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max3(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + map[i][j]

print(dp[n-1][m-1])