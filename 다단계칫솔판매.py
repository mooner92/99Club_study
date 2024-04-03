"""
import math
def solution(enroll, referral, seller, amount):
    answer = [0 for _ in range(len(enroll))]
    def trace(anc,cost):
        idx = enroll.index(anc)
        try:
            if referral[referral.index(idx)]!="-":
                answer[idx]+=cost
            else:
                answer[idx]+=math.floor(cost*90//100)
                trace(referral[referral.index(idx)],math.floor(cost*10//100))
    
    for i,d in enumerate(seller,start=0):
        trace(d,amount[i])

    return answer
"""

import math


def solution(enroll, referral, seller, amount):
    answer = {name: 0 for name in enroll}
    parent = {child: parent for child, parent in zip(enroll, referral)}
    # child(직원)과 parent(상사)간의 매핑

    def trace(name, revenue):
        if name == "-" or revenue == 0:  # 수입이 0원이거나 못팔았을 때 리턴
            return
        parent_revenue = revenue // 10  # 수수료 10%
        answer[name] += revenue - parent_revenue  # 순이익
        trace(parent[name], parent_revenue)  # 상사의 상사를 재귀를 통한 검색

    for s, a in zip(seller, amount):
        trace(s, a * 100)

    return [answer[name] for name in enroll]


###
