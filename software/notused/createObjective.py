
from operator import itemgetter, attrgetter

ct = 0
i = 0
lines = []
numberIndex = []
newIndex = []
objectiveIndex = []

# read the question file and store it into an array
# note the NEW and objective markers for each question
ff = open("all_mc_edited.txt","r")
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

        # determine if obj is a floating point number
        isfloat=1
        try:
            float(obj)
        except ValueError:
            isfloat = 0

        # if it is a floating point number, convert it - otherwise append 9999
        if isfloat== 1:
            objectiveIndex.append(float(obj))
        else:
            objectiveIndex.append(9999)
    i = i + 1

ff.close()

print len(objectiveIndex)

exit()



# find the end index for each question
endIndex = []
for i in range(len(newIndex)-1):
    endIndex.append( newIndex[i+1] )
endIndex.append(len(lines))



# copy the data into an array including a new index
lt = []
for i in range(len(newIndex)):
    lt.append( (numberIndex[i], objectiveIndex[i]) )

# sort the array by the index
slist = sorted(lt, key=itemgetter(1))

      
# using the sorted list, print things out in the new order
for r in range(len(slist)):
    ii = slist[r]
    jj = ii[0]
    istart = newIndex[jj]
    iend = endIndex[jj]

    for k in range(istart, iend):
        print lines[k]
    


