'''
   @ 2019.12.24 ush
   * 백준 알고리즘 - 1062 가르침 (https://www.acmicpc.net/problem/1062)
   * python (PyPy3)

   * bit mask

   * N개의 단어가 주어졌을 때, k 개의 글자로만 이루어진 단어의 개수를 고르는 문제
   
   * '각 단어가 어떤 알파벳으로 이루어져있는지'가 중요하다.
   * 따라서 단어를 이루는 알파벳을 비트로 나타내는 bitmask를 이용한다.

'''

def count (words, mask):
    cont = 0
    for word in words :
        if word & ((1<<26)-1-mask) == 0 : #다 배운거
            cont +=1
    return cont

def go(index, k, mask, words, end):
    if k < 0 :
        return 0
    if index == end :
        return count(words, mask)

    answer = 0

    #include index
    temp = go (index+1, k-1, mask|(1<<index), words, end)
    if answer < temp :
        answer = temp

    #exclude index
    if index not in [0, 2, 8, 13, 19]:
        temp = go (index+1, k, mask, words, end)
        if answer < temp :
            answer = temp
    return answer

n, k = map(int,input().split())
words=[0]*n

for i in range(0, n):
    word = str(input())
    for w in word:
        words[i] |= (1<<(ord(w)-ord('a')))

print(go(0, k, 0, words, 26))