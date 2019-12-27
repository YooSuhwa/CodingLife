
import math
def findPrimes (n):
    isPrime = [1]*n
    maxLength = math.ceil(math.sqrt(n))

    for i in range(2, maxLength):
        if isPrime[i]==1:
            for j in range(i+i, n, i):
                isPrime[j] = 0

    return [i for i in range(2, n) if isPrime[i]]

find = int(input())

primes = findPrimes(find+1)

left = right = 0
sum = primes[right]

answer = 0
number = 0
n = len(primes)

while left <= right and right < n:
    if sum < find:
        right += 1
        if right < n:
            sum += primes[right]

    elif sum == find:
        answer += 1
        right += 1
        if right < n:
            sum += primes[right]

    elif sum > find:
        sum -= primes[left]
        left += 1
        if left > right and left < n:
            right = left
            sum = primes[left]
print(answer)
