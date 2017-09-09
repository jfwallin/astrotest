fn = "questionlist.txt"
f = open(fn, "r")

qq = []
for l in f:
    
    if l.find("x") == 0:
        
        right = l.find(":")
        left = l.find(")")

#        print l[left+2:right]
        qq.append(int( l[left+2:right]))


f.close()


qf = qq.sort()

for q in qq:
    print q
