# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 2,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 
# 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

queue = deque()
N = int(input())
for i in range(N):
    com = input().split()
    if com[0] == 'push':
        queue.append(com[1])
    elif com[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif com[0] == 'size':
        print(len(queue))
    elif com[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif com[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif com[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)