def solution(storey):
    ans = 0
    while storey != 0:
        n = storey % 10
        if 6 <= n:
            ans += 10 - n
            storey += 10 - n
        elif n == 5 and (storey // 10) % 10 >= 5:
            ans += 10 - n
            storey += 10 - n
        else:
            ans += n
        storey //= 10
    return ans
