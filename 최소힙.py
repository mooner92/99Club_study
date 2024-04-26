
import sys
import heapq

a = int(sys.stdin.readline())
max_heap = []

for i in range(a):
    b = int(sys.stdin.readline())
    if b == 0:
        if not max_heap:
            print(0)
        else:
            print(heapq.heappop(max_heap))
    else:
        heapq.heappush(max_heap, b)

####