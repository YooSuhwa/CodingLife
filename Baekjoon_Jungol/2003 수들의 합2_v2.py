'''
   @ ush 2019/12/26
   * 백준 알고리즘 - 2003 수들의 합2 (https://www.acmicpc.net/problem/2003)
   * python

   * 수열의 i번째부터 j번째 수까지의 합이 find가 되는 경우의 수 구하기
   * 1. left/right 포인터를 둔다. (left < right)
   * 2. 만약 sum <= find 라면 right++ 
   * 3. 만약 sum > find 라면  left ++
'''
n, find = map(int, input().strip().split(' '))
arr = list(map(int, input().split()))

answer = 0

left = 0
right = 0
sum = arr[right]

while(True):
    if left>right or right>=n:
        break
    if sum < find :
        right += 1
        if right >= n :
            break
        sum += arr[right]
    elif sum == find :
        answer += 1
        right += 1
        if right >= n :
            break
        sum += arr[right]
    else :
        sum -= arr[left]
        left += 1
        if left > right and left < n:
            right = left
            sum = arr[left]

print(answer)