'''
   @ ush 2019/12/26
   * 백준 알고리즘 - 2003 수들의 합2 (https://www.acmicpc.net/problem/2003)
   * python (PyPy3)

   * 수열의 i번째부터 j번째 수까지의 합이 find가 되는 경우의 수 구하기
'''
n, find = map(int, input().strip().split(' '))
arr = list(map(int, input().split()))

answer = 0

for i in range(0, n):
    sum = 0
    for j in range(i, n):
        sum += arr[j]
        if sum == find :
            answer += 1
        elif sum > find :
            break

print(answer)