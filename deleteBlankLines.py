import sys
openFile = open('./new.txt','w')

with open("./run.txt") as f:
    for line in f:
        if not line.isspace():
            openFile.write(line)
openFile.close()
