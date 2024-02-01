# 📝 [2075] N번째 큰 수

import heapq

heap = []
n = int(input())

for _ in range(n):
    numbers = map(int, input().split())
    for number in numbers:
        if len(heap) < n: # heap의 크기를 n개로 유지
            heapq.heappush(heap, number)
        else:
            if heap[0] < number:
                heapq.heappop(heap)
                heapq.heappush(heap, number)
print(heap[0])
출처: https://kjhoon0330.tistory.com/entry/BOJ-2075-N번째-큰-수-Python [Jahni's Blog:티스토리]