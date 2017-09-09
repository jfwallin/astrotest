

ff = open("qfile","r")
ct = 1

for l in ff:
    l = l.strip()
    print ct, l
    ct = ct + 1

ff.close()
