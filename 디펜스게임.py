from heapq import heappush,heappop
def solution(n, k, enemy):
    answer = len(enemy)
    heap = []
    for i in range(min(k,len(enemy))):
        heappush(heap,enemy[i])
    for i in range(k,len(enemy)):
        if n<heap[0] and n<enemy[i]:
            return i
        if heap[0] < enemy[i]:
            heappush(heap,enemy[i])
            n-=heappop(heap)
        else:
            n-=enemy[i]
    return answer