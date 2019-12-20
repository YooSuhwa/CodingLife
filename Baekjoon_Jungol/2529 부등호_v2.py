'''
   @ 2019.12.20 ush
   * 백준 알고리즘 - 2529 부등호 (https://www.acmicpc.net/problem/2529)
   * python

   * 부등호 관계를 만족시키는 '최대 정수'와 '최소 정수'만 찾으면 된다.
   * 가장 큰 수를 찾기 위해서 9876... 순서 중 k+1개를 순열을 통해 부등호 만족하는 최대 정수 찾기
   * 가장 작은 수를 찾기 위해서 0123... 순서 중 k+1개를 순열을 통해 부등호 만족하는 최소 정수 찾기
'''
def check(num, inequality):
    for i in range(len(inequality)):
        if inequality[i] == '<' and num[i] > num[i+1]:
            return False
        if inequality[i] == '>' and num[i] < num[i+1]:
            return False
    return True

def nextPermutation(num):
    i = len(num)-1
    while i > 0 and num[i-1] >= num[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(num)-1
    while num[j] <= num[i-1]:
        j -= 1

    num[i-1],num[j] = num[j],num[i-1]

    j = len(num)-1
    while i < j:
        num[i],num[j] = num[j],num[i]
        i += 1
        j -= 1

    return True

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

inequality = []

k = int(input())
k+=1
inequality = list(input().split())
number = ['0','1','2','3','4','5','6','7','8','9']

minAnswer = ''
maxAnswer = ''

minCandidate = number[0:k]
maxCandidate = number[10-k :]
maxCandidate = sorted(maxCandidate, reverse=True)

while True :
    if check(minCandidate, inequality) :
        break
    if not nextPermutation(minCandidate):
        break

while True :
    if check(maxCandidate, inequality) :
        break
    if not prePermutation(maxCandidate):
        break

print(''.join(map(str,maxCandidate)))
print(''.join(map(str,minCandidate)))