def func(n):
    a_list = [0 for i in range(n)]
    
    if n < 3:
        return 1
    elif n < 5:
        return 2

    a_list[0], a_list[1], a_list[2] = 1, 1, 1
    a_list[3], a_list[4] = 2, 2
    
    for i in range(5, n):
        a_list[i] = a_list[i-2] + a_list[i-3]
        
    return a_list[-1]

a = int(input())
for i in range(a):
    b = int(input())
    print(func(b))

####