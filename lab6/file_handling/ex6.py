import string, os

if not os.path.exists("letters"):
    os.makedirs("letters")

path = "C:\\Users\\tuzel\\OneDrive\\Рабочий стол\\only\\pp2\\lab6\\file_handling\\letters"
os.chdir(path)
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)