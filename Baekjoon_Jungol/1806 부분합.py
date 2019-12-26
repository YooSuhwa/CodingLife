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
        sum -= arr[left]
        left += 1
        if left > right and left < n:
            right = left
            sum = arr[left]

if answer == -1 :
    answer = 0
print(answer)