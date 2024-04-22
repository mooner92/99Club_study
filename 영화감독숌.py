a = int(input())
sum=0
for i in range(666,10000000):
    c = str(i)
    if c.find("666")!=-1:
        sum+=1
    if sum==a:
        print(i)
        break
