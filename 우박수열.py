def solution(k, ranges):
    ds = [k,]
    weight = []
    answer = []
    cnt = 0
    while ds[cnt] != 1:
        if ds[cnt] % 2 == 0:
            ds.append(ds[cnt] / 2)
        else:
            ds.append(ds[cnt] * 3 + 1)
        weight.append((ds[cnt] + ds[cnt + 1]) / 2)
            
        cnt += 1
    for i in ranges:
        sum=0
        if(i[0]>i[1]+cnt):
            sum=-1
        else:
            for i in range(i[0],i[1]+cnt):
                sum+=weight[i]
        answer.append("{:.1f}".format(sum))

    return answer


