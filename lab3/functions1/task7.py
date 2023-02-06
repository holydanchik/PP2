def has33(nums):
    x = False
    for i in range(len(nums)):
        if not i == len(nums)-1:
            if nums[i]==3 and nums[i+1]==3:
                x = True
                return True
    if x == False:
        return False
    
print(has33([1,3,3,1]))
print(has33([1,3,1,3]))
print(has33([1,1,3,3]))
print(has33([3,3,1,1]))
print(has33([3,1,3,1]))
print(has33([3,1,1,3]))