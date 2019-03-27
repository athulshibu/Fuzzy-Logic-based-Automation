import pickle
import array
import os

path = "F:\TV Series\The Big Bang Theory\checker.txt"
episode,season = 24,12;
matrix = [[0 for x in range(episode)] for y in range(season)]
exists = os.path.isfile(path)

if exists:
    with open(path,'rb') as fp:
        matrix = pickle.load(fp)

count = [0,0,0,0,0,0,0,0,0,0,0,0]
counter_path = "F:\TV Series\The Big Bang Theory\The Big Bang Theory Season "
for i in range(1,13):
    for name in os.listdir(counter_path + str(i)):
        if name.endswith("mkv") or name.endswith("mp4"):
           count[i-1] = count[i-1] + 1
for i in range(0,5):
    print(" ",end=" ")
for i in range(1,25):
    print(str(i),end=" ")
print()

for i in range(0,12):
    if i<9:
        print("Season " + str(i+1) + " ",end=" ")
    else:
        print("Season " + str(i+1),end=" ")
    for j in range(0,24):
        if j>=count[i]:
            if j>=9:
                print("*",end="  ")
            else:
                print("*",end=" ")
        else:
            if j>=9:
                print(str(matrix[i][j]),end="  ")
            else:
                print(str(matrix[i][j]),end=" ")
    print()
input()
