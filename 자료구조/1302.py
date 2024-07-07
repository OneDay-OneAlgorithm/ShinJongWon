# 📝 [1302] 베스트셀러

import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
book = {}
for i in range(N):
    name = input()
    if name not in book:
        book[name] = 1
    else:
        book[name] += 1

book = list(book.items())
book.sort(key = lambda x : (-x[1],x[0]))
print(book[0][0])