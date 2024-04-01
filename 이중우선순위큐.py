# from queue import PriorityQueue
def solution(operations):
    answer = []
    quee = []
    for i in operations:
        t = i.split()
        if t[0] == "I":
            quee.append(int(t[1]))
        elif len(quee) != 0:
            if int(t[1]) == 1:
                quee.pop(0)
            else:
                quee.pop(len(quee) - 1)
        quee.sort(reverse=True)
    if len(quee) == 0:
        answer.extend([0, 0])
    else:
        answer.extend([quee[0], quee[len(quee) - 1]])

    return answer
