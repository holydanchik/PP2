def histogram(nums):
    hist = []
    for i in range(len(nums)):
        line = str()
        for j in range(nums[i]):
            line += '*'
        hist.append(line)
    for x in hist:
        print(x)

histogram([4, 9, 7])