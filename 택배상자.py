"""
def solution(order):
    ds = [i for i in range(1,len(order)+1)]
    sta = []
    g = len(order)
    answer=0
    for i in range(len(ds)):
        if(ds[0]==order[0]):
            break
        else:
            sta.append(ds[0])
            ds.pop(0)
    for i in range(g):
        if sta:
            if sta[-1]==order[0]:
                answer+=1
                sta.pop()
                order.pop(0)
        if ds:
            if ds[0]==order[0]:
                answer+=1
                ds.pop(0)
                order.pop(0)
        
    return answer
"""
