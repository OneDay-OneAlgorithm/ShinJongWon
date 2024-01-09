# 📝 [1966] 프린트 큐
# 첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.

import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for i in range(T):
    queue = deque()
    queue2 = deque()
    ct = 1
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for j in range(N):
        queue.append(arr[j])
        queue2.append(j)

    while True:
        if queue[0] == max(queue):
            if queue2[0] == M:
                print(ct)
                break
            else:
                queue.popleft()
                queue2.popleft()
                ct += 1
        else:
            queue.rotate(-1)
            queue2.rotate(-1)

