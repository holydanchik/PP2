# with open("E:\\test\\good.txt") as f:
    # print(sum(1 for _ in f))
    
count=0
with open ("E:\\test\\good.txt",'rb') as f:
    for line in f:
        count+=1

print(count)