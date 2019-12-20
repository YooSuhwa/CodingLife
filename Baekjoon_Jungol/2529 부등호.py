'''
   @ 2019.12.20 ush
   * 백준 알고리즘 - 2529 부등호 (https://www.acmicpc.net/problem/2529)
   * python

   * 부등호 관계를 만족시키는 '최대 정수'와 '최소 정수'만 찾으면 된다.
   * 가장 큰 수를 찾기 위해서 9876... 순서 중 k+1개를 순열을 통해 부등호 만족하는 최대 정수 찾기
   * 가장 작은 수를 찾기 위해서 0123... 순서 중 k+1개를 순열을 통해 부등호 만족하는 최소 정수 찾기

   * 개선점 : 메모리 제한때문에 미리 순열을 구해놓지 않는 방법 찾기
'''

import itertools
def check(num, inequality):
    for i in range(len(inequality)):
        if inequality[i] == '<' and num[i] > num[i+1]:
            return False
        if inequality[i] == '>' and num[i] < num[i+1]:
            return False
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
minCandidate = set(list(map("".join, itertools.permutations(minCandidate,k))))
maxCandidate = set(list(map("".join, itertools.permutations(maxCandidate,k))))

minCandidate = list(sorted(minCandidate))
maxCandidate= list(sorted(maxCandidate, reverse=True))

for num in minCandidate:
    if check(num, inequality) :
        minAnswer = num
        break
for num in maxCandidate:
    if check(num, inequality) :
        maxAnswer = num
        break

print(maxAnswer)
print(minAnswer)


