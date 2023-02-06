def unique_l(list):
    newList = []
    newList.append(list[0])
    for i in range (1, len(list)):
        if list[i] not in newList:
            newList.append(list[i])
    newList.sort()
    return newList

print(unique_l([1,2,2,3,3,3,4,5,4,5,6,6,66,7,0,9]))