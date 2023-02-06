def spy_game(nums):
    x = False
    i = 0
    while i<=len(nums)-3:
        if nums[i] == 0:
            if nums[i+1] == 0 and nums[i+2] == 7:
                x = True
                return True
        i += 1
    if x == False:
        return False        

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,0,7]))
print(spy_game([0,7,7,2,0,4,5,0]))
