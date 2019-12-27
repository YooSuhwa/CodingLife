'''
   @ ush 2019/12/27
   * 백준 알고리즘 - 1644 소수의 연속합 (https://www.acmicpc.net/problem/1644)
   * python

   * 백준 '2003 수들의 합'과 연관
   * 1. 주어진 수 이하의 모든 소수를 찾아 primes 리스트에 저장
   * 2. pirmes를 바탕으로 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구함
'''
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
