"""
def solution(bridge_length, weight, truck_weights):
    q = []
    i_sum = 0
    answer=0
    for i in truck_weights:
        if(i_sum+i<=weight):
            q.append(i)
            i_sum+=i
        else:
            i_sum=0
            answer+=bridge_length+len(q)-1
            while len(q)>0:
                #q.pop()
                print(q.pop())
            print("-------")
    return answer
"""

# 이 코드로 첫 시도를 하였지만 잘 안되어서 실패


def solution(bridge_length, weight, truck_weights):
    arr = [0] * bridge_length
    ans = 0
    k = 0
    while truck_weights:
        ans += 1
        if arr[0] != 0:
            k -= arr[0]
        arr.pop(0)
        arr.append(0)
        f = truck_weights[0]

        if k + f <= weight:
            arr[-1] = truck_weights.pop(0)
            k += f
    return ans + bridge_length
