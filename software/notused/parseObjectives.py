import re

fn = "Objectives_2016.txt"

ll = []
f = open(fn,"r")
for l in f:

    header = 0
    ll.append(l.strip())
    if l.find("L") == 0:
        lectureNumber= int(l[1:].split(":")[0])
        header = 1

    if header == 0:
        for i in range(10):
            a = l.find(str(i))
            if a == 0:
                aa  =  l.strip().split("\t")
              #  print aa
                o2= aa[1]
                objectiveNumber =  int(aa[0].split(".")[0])
                os = str(lectureNumber) + "." + str(objectiveNumber) + ", " + o2
                print os
f.close()
