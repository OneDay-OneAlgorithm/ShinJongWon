# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 
# 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

stack = []

for i in range(N):
    cmd = input().split()
    X = 0
    if len(cmd) == 2:
        X = cmd[1]
    cmd = cmd[0]

    if cmd == "push": 
        stack.append(X)
    elif cmd == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop(-1)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        print(0 if len(stack) else 1)
    elif cmd == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])