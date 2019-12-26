'''
   @ ush 2019/12/26
   * 백준 알고리즘 - 1806 부분합 (https://www.acmicpc.net/problem/1806)
   * python

   * 백준 '2003 수들의 합'과 연관
   * 구간의 합 중에서 합이 S이상인 것 중에서 가장 짧은 것을 구하는 문제
   * 1. left/right 포인터를 둔다. (left < right)
   * 2. 만약 sum <= find 라면 right++  and length 비교
   * 3. 만약 sum > find 라면  left ++  and length 비교
   * 4. 가장 짧은 length를 찾는 문제
'''
n, find = map(int, input().strip().split(' '))
arr = list(map(int, input().split()))

answer = -1

left = right = 0
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
        len = right-left + 1
        if (answer > len) or answer == -1:
            answer = len
        right += 1
        if right >= n :
            break
        sum += arr[right]
    else:
        len = right - left + 1
        if (answer > len) or answer == -1:
            answer = len

        sum -= arr[left]
        left += 1
        if left > right and left < n:
            right = left
            sum = arr[left]

if answer == -1 :
    answer = 0
print(answer)