def solution(e, starts):
    answer = []
    ns = [0 for _ in range(e+1)]
    for i in range(1,e+1):
        for j in range(1,(e//i)+1):
            ns[i*j]+=1
    for st in starts:
        max=-1
        f=0
        for i in range(st,e+1):
            if max<ns[i]:
                max=ns[i]
                f=i
        answer.append(f)
    return answer