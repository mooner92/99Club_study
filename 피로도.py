def solution(k, dungeons):
    ans = -1

    def rec(k, n, ds):
        nonlocal ans
        for i, d in enumerate(ds):
            if n >= d[0]:
                nds = ds.copy()
                nds.pop(i)
                cnt = rec(k + 1, n - d[1], nds)
                if ans < cnt:
                    ans = cnt
        return k

    rec(0, k, dungeons)
    return ans
