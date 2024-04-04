def solution(maps):
    arrow = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    answer = []
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]

    def search(r, c, cnt):
        if maps[r][c] == "X" or visited[r][c]:
            return cnt
        visited[r][c] = 1
        cnt += int(maps[r][c])
        for a in arrow:
            r1, c1 = r + a[0], c + a[1]
            if 0 <= r1 < len(maps) and 0 <= c1 < len(maps[0]):
                cnt = search(r1, c1, cnt)
        return cnt

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if not visited[i][j] and maps[i][j] != "X":
                result = search(i, j, 0)
                if result:
                    answer.append(result)
                # 탐색 후 visited를 초기화해야 하는 경우 아래 코드의 주석을 해제하세요.
                # visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    answer.sort()
    return answer


"""
def solution(maps):
    arrow = [[-1,0],[1,0],[0,-1],[0,1]]
    answer = [0 for _ in range(10000)]
    cnt=0
    visited = [[0 for _ in range(len(maps))] for _ in range(len(maps))]
    def search(r,c):
        for a in arrow:
            r1,c1 = r+a[0],c+a[1]
            if r1>=0 and r1<len(maps) and c1>=0 and c1<len(maps):
                if(visited[r1][c1]==0):
                    visited[r1][c1]=1
                    if(maps[r1][c1]!='X'):
                        answer[cnt]+=int(maps[r1][c1])
                        search(r1,c1)
                    
    for i in range(len(maps)):
        for j in range(len(maps)):
            search(i,j)
            cnt+=1
                    
    answer.sort()
    return 
"""
