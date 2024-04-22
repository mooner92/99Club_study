# import heapq

# a = int(input())

# max_heap = []
# for i in range(a):
#     b = int(input())
#     if b==0:
#         c=0
#         if len(max_heap)!=0:
#             c = heapq.heappop(max_heap)*-1
#         print(c)
#     else:
#         heapq.heappush(max_heap,b*-1)

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
            print(heapq.heappop(max_heap) * -1)
    else:
        heapq.heappush(max_heap, -b)