from collections import deque

def solution(n, roads, sources, destination):

    graph = [[] for _ in range(n+1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    distances = [-1] * (n + 1)
    distances[destination] = 0  
    
    queue = deque([destination])
    while queue:
        current = queue.popleft()
        for next in graph[current]:
            if distances[next] == -1:  
                distances[next] = distances[current] + 1
                queue.append(next)

    answer = [distances[source] for source in sources]
    return answer
