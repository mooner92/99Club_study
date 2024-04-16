def solution(board):
    answer = -1
    global xt, ot  # 전역 변수 선언
    xt, ot = 0, 0

    def verify():
        global xt, ot  # 전역 변수 사용을 위한 선언
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    xt += 1
                elif board[i][j] == 'O':
                    ot += 1
        x, o = 0, 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    x += 1
                elif board[i][j] == 'O':
                    o += 1
            if x == 3:
                return 1
            elif o == 3:
                return 2
            x, o = 0, 0

        for i in range(3):
            for j in range(3):
                if board[j][i] == 'X':
                    x += 1
                elif board[j][i] == 'O':
                    o += 1
            if x == 3:
                return 1
            elif o == 3:
                return 2
            x, o = 0, 0

        # 대각선 검사 개선
        x, o = 0, 0
        for i in range(3):
            if board[i][i] == 'X':
                x += 1
            elif board[i][i] == 'O':
                o += 1
        if x == 3:
            return 1
        elif o == 3:
            return 2

        x, o = 0, 0
        for i in range(3):
            if board[i][2-i] == 'X':
                x += 1
            elif board[i][2-i] == 'O':
                o += 1
        if x == 3:
            return 1
        elif o == 3:
            return 2
            
        return 0

    d = verify()
    #print(xt,ot)
    if d == 1 or d == 2:
        if d == 2:
            if ot == xt+1:
                return 1
            else:
                return 0
        elif d==1:
            if xt==ot:
                return 1
            else:
                return 0
    elif d==0:
        if ot-xt==0 or ot-xt==1:
            return 1
        else:
            return 0
    return 1
