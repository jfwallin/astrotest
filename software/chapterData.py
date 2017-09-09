import string
import re
import qb

keyString = "Answer:"
KEY = 100
DIFF = 200
diffString = "Diff:"
SECTION = 300
sectionString = "Section Ref:"
QUESTION = 500
mcString = ["A) ", "B) ", "C) ", "D) ", "E) "]
mcOFFSET = 1000
iGroup = []
iKey = []
iSection = []
iDiff = []


questionGroup = ["True/False Questions","Multiple-Choice Questions","Fill-in-the-Blank Questions","Short Answer Questions","Essay Questions"]

class chapterFile:
  def __init__(self):
      ct = 0

  def readFile(self,fname,lecture, clist):

      ct = 0
      kk =open(fname,"r")
      for line in kk:
          line = line.strip()
          clist.append(line)
          ct = ct + 1
      kk.close()        

  def findQuestionBlocks(self, iNotate, clist):

    # allocate the space for the arrays
    for i in range(0, len(clist)):
      iNotate.append(0)
    for j in range(0,len(questionGroup)):
      iGroup.append(0)

    # fix percent marks
    for i in range(0, len(clist)):
      clist[i] = re.sub("\%","\\\%",clist[i])
      clist[i] = re.sub("________","\\underline{\\hspace{0.5in}}",clist[i])
      clist[i] = re.sub("_______","\\underline{\\hspace{0.5in}}",clist[i])
      clist[i] = re.sub("______","\\underline{\\hspace{0.5in}}",clist[i])
      clist[i] = re.sub("_____","\\underline{\\hspace{0.5in}}",clist[i])
     # clist[i] = re.sub("________","\\underline\{\\hspace\{0.5in\}\}",clist[i])
     # clist[i] = re.sub("________","\\underline\{\\hspace\{0.5in\}\}",clist[i])
     # clist[i] = re.sub("________","\\underline\{\\hspace\{0.5in\}\}",clist[i])
        

    # find the question group markings
    for i in range(0, len(clist)):
      for j in range(0,len(questionGroup)):
        if (string.find(clist[i],questionGroup[j]) >= 0):
          iGroup[j]= i
          iNotate[i] = -j

    # find the locations of the answers
    for i in range(0, len(clist)):
      if (string.find(clist[i],keyString) >= 0):
        iKey.append(i)
        iNotate[i] = KEY

    # find the locations of the  difficulties
    for i in range(0, len(clist)):
      if (string.find(clist[i],diffString) >= 0):
        iDiff.append(i)
        iNotate[i] = DIFF

    # find the locations of the sections
    for i in range(0, len(clist)):
      if (string.find(clist[i],sectionString) >= 0):
        iSection.append(i)
        iNotate[i] = SECTION


    # find the multiple choice question answers
    for i in range(0, len(clist)):
      for j in range(0, len(mcString)):
        if (string.find(clist[i],mcString[j]) >= 0):
          iNotate[i] = j + mcOFFSET

    # find the possible MC question starting points
    for i in range(0, len(clist)):
      iloc = string.find(clist[i],")")
      if (iloc >= 0 and iloc < 3 and iNotate[i] == 0):
          iNotate[i] = QUESTION









  def printAnnotatedList(self, iNotate, clist):
    istart = iGroup[0]
    iend = iGroup[2]
    for i in range(istart, iend):
      print iNotate[i], " > ", clist[i]


  def processMCQuestions(self, chapter, iNotate, clist, qlist):

    qstart = []
    qend = []

    # find the starting and ending point of question blocks
    istart = iGroup[1]
    iend = iGroup[2]

    for i in range(istart, iend):
      if (iNotate[i] == QUESTION):
        qstart.append(i)
      if (iNotate[i] == SECTION):
        qend.append(i)

    for j in range(0,len(qstart)):
      q = qb.questionBlock()
      q.fillMC(iNotate, clist, qstart[j],qend[j])
      q.setChapter(chapter)
      qlist.append(q)


  def processTFQuestions(self, chapter, iNotate, clist, qlist):

    qstart = []
    qend = []

    # find the starting and ending point of question blocks
    istart = iGroup[0]
    iend = iGroup[1]

    for i in range(istart, iend):
      if (iNotate[i] == QUESTION):
        qstart.append(i)
      if (iNotate[i] == SECTION):
        qend.append(i)

    for j in range(0,len(qstart)):
      q = qb.questionBlock()
      q.fillTF(iNotate, clist, qstart[j],qend[j])
      q.setChapter(chapter)
      qlist.append(q)


  def writeMCQuestionFile(self, newname, qlist):
    f = open(newname,"w")
    for q in qlist:
      q.WRITE(f)
    f.close()


  def readMCQuestionFile(self, newname, clist):
    f1 = open(newname,"r")
    for line in f1:
      line = line.strip()
      clist.append(line)
    f1.close()        

  def processMCQuestionFile(self, clist, qlist):

    BREAK = 1000
    iNotate = []
    # find the question breaks
    for i in range(0, len(clist)):
      line = clist[i]
      iNotate.append(0)
      if (string.find(line,"NEW") == 0):
        iNotate[i] = BREAK

    iNotate.append(1000)

    bstart = []
    bend = []
    bstart.append(0)
    for i in range(0, len(clist)):
      if (iNotate[i] == BREAK):
        bstart.append(i)
        bend.append(i)
    bend.append(len(clist))

    

    for j in range(1, len(bstart)):
      q = qb.questionBlock()
      q.readMCBlock(clist, bstart[j],bend[j])
      qlist.append(q)
      






    


