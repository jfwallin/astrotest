
from operator import itemgetter, attrgetter

ct = 0
i = 0
lines = []
numberIndex = []
newIndex = []
objectiveIndex = []
ff = open("all_mc.txt","r")
for l in ff:
    l = l.strip()
    lines.append(l)
    ii = l.find("NEW")
    if (ii == 0):
        newIndex.append(i)
        numberIndex.append(ct)
        ct = ct + 1
        
    jj = l.find("objective")
    if jj == 0:
        oo = l.split("=")
        obj = oo[1]
        objectiveIndex.append(obj)

    i = i + 1

ff.close()

endIndex = []
for i in range(len(newIndex)-1):
    endIndex.append( newIndex[i+1] )
endIndex.append(len(lines))

lt = []
for i in range(len(newIndex)):
    lt.append( (numberIndex[i], objectiveIndex[i]) )


slist = sorted(lt, key=itemgetter(1))

    
#    print newIndex[i], endIndex[i], numberIndex[i], objectiveIndex[i]
    


for r in range(len(slist)):
    ii = slist[r]
    jj = ii[0]
    istart = newIndex[jj]
    iend = endIndex[jj]
#    print ii, istart, iend

    for k in range(istart, iend):
        print lines[k]
    
print len(newIndex), len(numberIndex), len(objectiveIndex), len(endIndex)

