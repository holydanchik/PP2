list = ['Happy', 'International', 'Womens', 'Day']
with open("E:\\test\\good.txt", "w") as myfile:
        for c in list:
                myfile.write("%s\n" % c)

content = open("E:\\test\\good.txt")
print(content.read())