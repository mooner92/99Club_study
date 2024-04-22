a = int(input())
sum=1
for i in range(667,1000000000):
    c = str(i)
    if c.find("666")!=-1:
        sum+=1
    if sum==a:
        print(i)
        break
