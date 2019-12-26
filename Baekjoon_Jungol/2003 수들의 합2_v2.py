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

print(answer)