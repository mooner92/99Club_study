def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    costs.sort(key=lambda x: x[2])  # 비용을 기준으로 오름차순 정렬
    parent = [i for i in range(n)]  # 부모 테이블 초기화
    answer = 0

    for cost in costs:
        a, b, c = cost  # a섬과 b섬을 연결하는 비용 c
        # 두 섬의 루트가 다르다면, 즉 두 섬이 서로 다른 집합에 속해 있다면
        if find(parent, a) != find(parent, b):
            union(parent, a, b)  # 두 섬을 연결(집합 합치기)
            answer += c  # 해당 다리의 비용을 결과에 추가

    return answer

###