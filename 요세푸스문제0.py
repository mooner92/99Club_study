from collections import deque

def main():
    k = deque()
    tc, t = map(int, input().split())
    for i in range(tc):
        k.append(i + 1)
    
    result = []
    while k:
        k.rotate(-(t-1))
        result.append(str(k.popleft()))
    
    print("<" + ", ".join(result) + ">")

if __name__ == "__main__":
    main()
