def solution(m, n, startX, startY, balls):
    answer = []
    for i in balls:
        res = 0
        if startY == i[1]:
            h = min(i[1], n - i[1])
            t = (m - startX + m - i[0]) if (startX > i[0]) else (startX + i[0])
            res = min((2 * h) ** 2 + abs(i[0] - startX) ** 2, t**2)
        elif startX == i[0]:
            h = min(i[0], m - i[0])
            t = (n - startY + n - i[1]) if (startY > i[1]) else (startY + i[1])
            res = min((2 * h) ** 2 + abs(i[1] - startY) ** 2, t**2)
        else:
            res = min(
                abs(n + (n - i[1]) - startY) ** 2
                + abs(max(i[0] - startX, startX - i[0])) ** 2,
                abs(-1 * i[0] - startX) ** 2
                + abs(max(startY - i[1], i[1] - startY)) ** 2,
                abs(m + (m - i[0]) - startX) ** 2
                + abs(max(startY - i[1], i[1] - startY)) ** 2,
                abs(-1 * i[1] - startY) ** 2
                + abs(max(startX - i[0], i[0] - startX)) ** 2,
            )

        answer.append(res)
    return answer


####
