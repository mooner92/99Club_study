def solution(n):
    st = [[0 for _ in range(1000)] for _ in range(1000)]
    answer = []
    t = 1
    for i in range(n):
        u = i // 3
        if i % 3 == 0:
            for j in range(0, n - u * 3):
                st[u * 2 + j][u] = t
                # print("{0} {1} {2}".format(u*2+j ,u,t))
                t += 1

        elif i % 3 == 1:
            for j in range(0, n - u * 3 - 1):
                st[n - u - 1][u + 1 + j] = t
                # print("{0} {1} {2}".format(n-u-1,u+1+j,t))
                t += 1

        elif i % 3 == 2:
            for j in range(0, n - u * 3 - 2):
                st[n - 2 - u - j][n - 2 - (u * 2) - j] = t
                # print("{0} {1} {2}".format(n-2-u-j ,n-2-(u*2)-j,t))
                t += 1

        # print("\n\n")
    for i in range(n):
        for j in range(n):
            # print(st[i][j],end=' ')
            if st[i][j] != 0:
                answer.append(st[i][j])
                # print("{0} {1} {2}".format(i,j,st[i][j]))
        # print()

    return answer


###
