def switch(cnt):
    return {
        3 : 'A',
        2 : 'B',
        1 : 'C',
        0 : 'D',
        4 : 'E',
    }.get(cnt, -1)
for _ in range(3):
    arr = list(map(int, input().split(' ')))
    print(switch(arr.count(1)))