def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

def main():
    tc = int(input())
    for _ in range(tc):
        n, m = map(int, input().split())
        if n < (m - n):
            dummy = n
        else:
            dummy = (m - n)
        g = fact(m) // (fact(dummy) * fact(m - dummy))
        print(g)

if __name__ == "__main__":
    main()
