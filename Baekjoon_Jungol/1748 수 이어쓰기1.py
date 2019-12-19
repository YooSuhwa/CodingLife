'''
   @ 2019.12.19 ush
   * 백준 알고리즘 - 1748 수 이어쓰기1 (https://www.acmicpc.net/problem/1748)
   * python

   * N의 범위 1~100000000
   * N이 너무 크기 때문에, 실제로 수를 만드는 것은 어렵다.
   * 따라서 수의 자리수별로 나누어서 문제를 해결하기
   
'''
num = int(input()) #100000000 08

str9 = '9'
answer = 0

while(1):
    int9 = int(str9)
    temp = 0
    if num <9  :
        answer= (num-1+1)
        break
    if int9 >= num :
        str99 = str9[:len(str9)-1]
        int9 = int(str99)
        temp = num - (int9+1) +1
        answer += temp * len(str9)
        break
    else :
        temp = pow(10, (len(str9) - 1))
        temp *= 9
        temp *= len(str9)
        answer+= temp
        str9 += '9'

print(answer)
