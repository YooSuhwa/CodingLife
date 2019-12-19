'''
   @ 2019.12.19 ush
   * 백준 알고리즘 - 1748 수 이어쓰기1 (https://www.acmicpc.net/problem/1748)
   * python

   * N의 범위 1~100000000
   * N이 너무 크기 때문에, 실제로 수를 만드는 것은 어렵다.
   * 따라서 수의 자리수별로 나누어서 문제를 해결하기

'''
num = int(input()) #100000000 08

answer = 0

start = 1
end =9
length = 1


while(1):
    if num < end :
        end = num
        break
    answer += (end - start +1) * length

    start *=10
    end = start*10-1
    length +=1
answer += (end - start +1) * length
print(answer)