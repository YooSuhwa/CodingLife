'''
   @ 2019.12.21 ush
   * 백준 알고리즘 - 1339 단어수학 (https://www.acmicpc.net/problem/1339)
   * python

   * 만들 수 있는 합의 '최대값'만 구하면 되므로 순열을 이용한 브로드포스 방법
   * 1. 연산 알파벳을 입력을 받으면 집합을 통해 필요한 알파벳의 갯수를 알아냄 (중복제거)
   * 2. 중복이 제거된 알파벳이 k개라면, 9876... 순으로 k개를 넣어 순열을 이용해 계산
   * 3. 계산된 값들 중 최대값을 찾는다.과
   
   * 개선점 : 시간초
'''
def calculation(calcul, letters, numbers):
    dict ={}
    sum = 0
    for i in range(0, len(letters)):
        dict[letters[i]] = numbers[i]
    for cal in calcul:
        now = 0
        for c in cal :
            now = now *10 + dict[c]
        sum += now

    return sum

def prePermutation(num):
    i = len(num)-1
    while i > 0 and num[i-1] <= num[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(num)-1
    while num[j] >= num[i-1]:
        j -= 1

    num[i-1],num[j] = num[j],num[i-1]

    j = len(num)-1
    while i < j:
        num[i],num[j] = num[j],num[i]
        i += 1
        j -= 1
    return True

calcul = []
letters = set()

N = int(input())
answer = 0
for i in range(0, N):
    calcul.extend(input().split())
    for letter in calcul[i]:
        letters.add(letter)

letters = sorted(letters)
size = len(letters)

numbers = [9-i for i in range(0, size)]

while True :
    num = calculation(calcul, letters, numbers)
    if num > answer :
        answer = num

    if not prePermutation(numbers) :
        break

print(answer)
