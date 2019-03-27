import os
from random import randint
import pickle
import array

path = "F:\TV Series\The Big Bang Theory\checker.txt"
count = [0,0,0,0,0,0,0,0,0,0,0,0]
episode,season = 24,12;
matrix = [[0 for x in range(episode)] for y in range(season)]
exists = os.path.isfile(path)

counter_path = "F:\TV Series\The Big Bang Theory\The Big Bang Theory Season "
for i in range(1,13):
    for name in os.listdir(counter_path + str(i)):
        if name.endswith("mkv") or name.endswith("mp4"):
           count[i-1] = count[i-1] + 1
    
if exists:
    with open(path,'rb') as fp:
        matrix = pickle.load(fp)
else:
    with open(path,'wb') as fp:
        pickle.dump(matrix,fp)

checker = 1
x = 0
y = 0
while checker!=0:
    x = randint(1,season+1)
    y = randint(1,count[x-1])
    file_path = "F:\TV Series\The Big Bang Theory\The Big Bang Theory Season " + str(x)
    counter = 0
    print(file_path)
    for name in os.listdir(file_path):
        print(name)
        if name.endswith("mkv") or name.endswith("mp4"):
            counter = counter + 1
        if counter == y:
            if randint(0,9)>matrix[x][y]:
                print(x,y,matrix[x][y])
                file_path = file_path + "\\" + name
                print(file_path)
                os.startfile(file_path)
                checker = 0
            else:
                checker = 0
            break
matrix[x-1][y-1] = matrix[x-1][y-1] + 1
print(x,y,matrix[x-1][y-1])
with open(path,'wb') as fp:
    pickle.dump(matrix,fp)
print("Success")
