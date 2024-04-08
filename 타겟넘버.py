def solution(numbers, target):
    answer = 0
    visited = [0 for _ in range(len(numbers)+1)]
    def dfs(n,t):
        nonlocal answer
        if t==target and n == len(numbers):
            answer+=1
            return 0
        visited[n] = 1
        if n+1<=len(numbers):
            if not visited[n+1]:
                dfs(n+1,t-numbers[n])
                dfs(n+1,t+numbers[n])
        visited[n] = 0
    dfs(0,0)
    
    return answer