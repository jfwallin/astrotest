import string
import testAnnotation
import random
from operator import itemgetter, attrgetter


keyString = "Answer:"
KEY = 100
DIFF = 200
diffString = "Diff:"
SECTION = 300
sectionString = "Section Ref:"
QUESTION = 500
mcString = ["A) ", "B) ", "C) ", "D) ", "E) "]
mcOFFSET = 1000


class questionBlock:
  def __init__(self):
    self.index = 0
    self.question = ""
    self.answer = []
    self.originalAnswer = []
    self.originalNanswer = 0
    self.key = ""
    self.diff = 0
    self.source="homework"
    self.sectionRef =""
    self.scramble = "Y"
    self.include = 0
    self.objective = 0
    self.globalIndex = -1
    self.localIndex = -1
    self.ilist = []
    self.answerOrder = []
    self.hasImage = 0
    self.imageName = ""
    self.answerOrder.append(0)
    self.answerOrder.append(1)
    self.answerOrder.append(2)
    self.answerOrder.append(3)
    self.answerOrder.append(4)

 
  def fillMC(self, iNotate, clist, istart, iend):
    self.index = 0
    self.question = ""
    self.answer = []
    self.key = ""
    self.diff = 0
    self.sectionRef =""
    self.scramble = "Y"
    self.objective = 0
    self.nanswer = 0
    self.originalNanswer = 0
    self.originalAnswer = []
    self.originalKey = ""
    self.selected = 0
    self.type = "MC"
    self.globalIndex = 0

    for i in range(istart,iend+1):
      if (iNotate[i] == QUESTION):
        sq = clist[i].split(") ")
        self.index =  int(sq[0])
        self.question = sq[1]

      if (iNotate[i] == 0):
        self.question = self.question + " " + clist[i]

      if (iNotate[i] == DIFF):
        sd = clist[i].split(": ")
        self.diff = int(sd[1])

      if (iNotate[i] == SECTION):
        ss = clist[i].split(":")
        self.sectionRef = ss[1]

      if (iNotate[i] == KEY):
        ss = clist[i].split(": ")
        self.key = ss[1]
        self.originalKey = ss[1]

        for k in range(0, len(self.answer)):
          if (string.find(self.key, mcString[k][0])>0):
            self.nanswer = k
            self.originalNanswer = k

      if (iNotate[i] >= OFFSET):
        sa = clist[i].split(") ")
        self.answer.append(sa[1])
        self.originalAnswer.append(sa[1])
    self.scramble = "Y"



  def setChapter(self, chapter):
    self.chapter = chapter

  def fillTF(self, iNotate, clist, istart, iend):
    self.index = 0
    self.question = ""
    self.answer = []
    self.key = ""
    self.diff = 0
    self.sectionRef =""
    self.scramble = "Y"
    self.nanswer = 0
    self.originalNanswer = 0
    self.originalAnswer = []
    self.originalKey = ""
    self.selected = 0
    self.type = "TF"

    for i in range(istart,iend+1):
      if (iNotate[i] == QUESTION):
        sq = clist[i].split(") ")
        self.index = int(sq[0])
        self.question = sq[1]

      if (iNotate[i] == 0):
        self.question = self.question + " " + clist[i]

      if (iNotate[i] == DIFF):
        sd = clist[i].split(": ")
        self.diff = int(sd[1])

      if (iNotate[i] == SECTION):
        ss = clist[i].split(":")
        self.sectionRef = ss[1]

      if (iNotate[i] == KEY):
        ss = clist[i].split(":")
        if ( (string.find(ss[1],"T")>=0) or (string.find(ss[1],"t") >=0)):
          self.key = "TRUE"
          self.originalKey = "TRUE"
          self.nanswer = 0
          self.originalNAnswer = 0
        else:
          self.key = "FALSE"
          self.originalKey = "FALSE"
          self.nanswer = 1
          self.originalNAnswer = 1
          
#        for k in range(0, len(self.answer)):
#          if (string.find(self.key, mcString[k][0])>0):
#            self.nanswer = k
#            self.originalNanswer = k

#      if (iNotate[i] >= mcOFFSET):
#        sa = clist[i].split(") ")
#        self.answer.append(sa[1])
#        self.originalAnswer.append(sa[1])
  
    self.originalAnswer.append("TRUE")
    self.originalAnswer.append("FALSE")
    self.answer.append("TRUE")
    self.answer.append("FALSE")
    self.scramble = "N"


  def addQuestion(self):
    self.selected = 1

  def PRINT(self):
    print "QUESTION> ",self.index
    print self.question
    for k in range(0, len(self.answer)):
      if (string.find(self.key, mcString[k][0])>0):
        sys.stdout.write("*")
      print mcString[k], self.answer[k]

    print self.key
    print self.diff
    print self.scramble
    print self.type
    print self.objective

  def WRITE(self,f):    
    f.write( "NEW\n" )
    f.write( "question=")
    f.write( self.question + "\n" )
    for k in range(0, len(self.answer)):
      f.write( "answer="  )
      f.write( self.answer[k] + "\n" )

    f.write("key=")
    f.write(str(self.nanswer) + "\n")
    f.write( "chapter=" )
    f.write( self.chapter + "\n")
#    self.chapter = chapter
    f.write( "index=" )
    f.write( str(self.index) + "\n" )
    f.write( "difficulty=" )
    f.write( str(self.diff) + "\n" )
    f.write( "source=" )
    f.write( str(self.source) + "\n" )
    f.write( "scramble=")
    f.write( self.scramble + "\n" )
    f.write( "type=")
    f.write( self.type + "\n" )
    f.write( "objective=")
    f.write( str(self.objective) + "\n" )
    



  def readMCBlock(self, clist, bstart, bend ):
    for i in range(bstart, bend):
      
      line = clist[i]
      if (string.find(line,"question=") == 0):
        stmp = line.split("=")
        self.question = stmp[1]
      if (string.find(line,"key=") == 0):
        stmp = line.split("=")
        self.nanswer = stmp[1]
      if (string.find(line,"chapter=") == 0):
        stmp = line.split("=")
        self.chapter = stmp[1]
      if (string.find(line,"index=") == 0):
        stmp = line.split("=")
        self.index = stmp[1]
      if (string.find(line,"difficulty=") == 0):
        stmp = line.split("=")
        self.difficulty = stmp[1]
      if (string.find(line,"source=") == 0):
        stmp = line.split("=")
        self.source = stmp[1]
      if (string.find(line,"scramble=") == 0):
        stmp = line.split("=")
        self.scramble = stmp[1]
      if (string.find(line,"answer=") == 0):
        stmp = line.split("=")
        self.answer.append(stmp[1])
      if (string.find(line,"type=") == 0):
        stmp = line.split("=")
        self.type= stmp[1]
      if (string.find(line,"objective=") == 0):
        stmp = line.split("=")
        self.objective= stmp[1]  
      if (string.find(line,"image=") == 0):
        stmp = line.split("=")
        self.imageName= stmp[1] 
        if self.imageName != "":
            self.hasImage = 1

      self.selected = 0




  def latexFullPrint(self, f):
    f.write("\\item ")
    f.write(self.question + "\n")
    f.write("\\begin{enumerate}\n")
    for k in range(0, len(self.answer)):
      f.write("\\item ")
      if (k == self.nanswer):
        f.write( "*" + self.answer[k] + "\n" )
      else:
        f.write( self.answer[k] + "\n" )
    f.write("\\end{enumerate}\n\n")
    f.write("Objective = "+self.objective + "\n")
    f.write("Chapter = " +self.chapter + "\n")
#    f.write("Index = " + str(self.index) + "\n")
#    f.write("Section = " + self.sectionRef + "\n")
#    f.write("Difficulty = " + str(self.diff)  +"\n")
    f.write("Source="+self.source + "\n")
    f.write("Scramble = " +self.scramble+ "\n")
    f.write("Selected = " + str(self.selected)+ "\n")
#    f.write("Global Index =" + str(self.globalIndex) + "\n")
    f.write("Type = "+ self.type + "\n")
    f.write("Objective"+self.objective +"\n")
    


  def latexCompactFullPrint(self, f):


    if self.hasImage == 0:
      w1 = "\\textwidth"
      w2 = "\\textwidth"
    else:
      w1 = "\\textwidth"
      w2 = "3.0in"
 

    f.write("\\begin{minipage}{"+w1+"}\n")
    f.write("\\begin{minipage}{"+w2+"}\n")

    f.write("\\item ")
#    f.write("("+ str(self.globalIndex) + ") ")
    f.write(self.question + "\n")
#    f.write("Global Index =" + str(self.globalIndex) + "\n")
    
#    f.write("\n")

    # find the maximum length for an answer
    mlength = 0
    for k in range(0, len(self.answer)):
      ll = len(self.answer[k])
      if (ll > mlength):
        mlength = ll 

    letters = ["(a) ","(b) ", "(c) ", "(d) ", "(e) "]



    nn = "1"
    if (mlength < 20):
      nn = "3"
    elif (mlength < 40):
      nn = "2"
    else:
      nn = "1"


    if self.hasImage == 1:
      nn = "1"
      if (mlength < 15):
        nn = "2"

    if (nn != "1"):  
      f.write("\\begin{multicols}{" + nn + "}\n")
    f.write("\\begin{enumerate} \n")
    f.write("\\setlength{\\itemsep}{1pt} \n")
    f.write("\\setlength{\\parskip}{0pt} \n")
    f.write("\\setlength{\\parsep}{0pt}\n")
    f.write("\\setlength{\\multicolsep}{1pt} \n")

    for k in range(0, len(self.answer)):
      f.write("\item ")
      if (k == int(self.nanswer)):
        f.write( "*" + self.answer[k]  )
      else:
        f.write( self.answer[k]  )
      f.write("\n")

    f.write("\\end{enumerate} \n")
    if (nn != "1"):
      f.write("\\vfill \n")
      f.write("\\end{multicols}\n")        
      f.write("\n")
    
    #f.write("\\\\ \n")
#    f.write("Answer  =" + str(self.nanswer)+ "\n")
    f.write("Objective = "+self.objective + "\n")
#    f.write("Chapter = " +self.chapter + "\n")
    f.write("Index = " + str(self.index) + "\n")
#    f.write("Section = " + self.sectionRef + "\n")
    f.write("Source = " + str(self.source)  +"\n")
#    f.write("Difficulty = " + str(self.diff)  +"\n")
    f.write("Scramble = " +self.scramble+ "\n")
#    f.write("Selected = " + str(self.selected)+ "\n")
    f.write("Type = "+ self.type + "\n")
#    f.write("Objective = " + str(self.objective) + "\n")
#    f.write("GlobalIndex = "+ str(self.globalIndex) + "\n")


    f.write("\\end{minipage}\n")
    if self.hasImage == 1:
      f.write("\\hspace{0.5in}\n")
      f.write("\\includegraphics[width=2in,height=1.5in,valign=c]{"+self.imageName+"}\n")
    f.write("\\end{minipage}\n")
    f.write("\\vskip 0.20in\n\n")



  def latexCompactStudentPrint(self, f):
#    f.write("\\begin{samepage} \n")

    
    iName = ""
    iName = "sunset.pdf"
    
    

    if self.hasImage == 0:
      w1 = "\\textwidth"
      w2 = "\\textwidth"
    else:
      w1 = "\\textwidth"
      w2 = "3.0in"
 

    f.write("\\begin{minipage}{"+w1+"}\n")
    f.write("\\begin{minipage}{"+w2+"}\n")
    f.write("\\item ")
    f.write(self.question + "\n")

    # find the maximum length for an answer
    mlength = 0
    for k in range(0, len(self.answer)):
      ll = len(self.answer[k])
      if (ll > mlength):
        mlength = ll 

    letters = ["(a) ","(b) ", "(c) ", "(d) ", "(e) "]

    nn = "1"
    if (mlength < 20):
      nn = "3"
    elif (mlength < 40):
      nn = "2"
    else:
      nn = "1"

    if self.hasImage == 1:
      nn = "1"
      if (mlength < 15):
        nn = "2"

    if (nn != "1"):  
      f.write("\\begin{multicols}{" + nn + "}\n")
    f.write("\\begin{enumerate} \n")
    f.write("\\setlength{\\itemsep}{1pt} \n")
    f.write("\\setlength{\\parskip}{0pt} \n")
    f.write("\\setlength{\\parsep}{0pt}\n")
    f.write("\\setlength{\\multicolsep}{1pt} \n")

    for k in range(0, len(self.answer)):
      f.write("\item ")
      f.write( self.answer[k]  )
      f.write("\n")
    f.write("\\end{enumerate} \n")

    if (nn != "1"):
      f.write("\\vfill \n")
      f.write("\\end{multicols}\n")        
      f.write("\n")
    f.write("\\end{minipage}\n")

    if self.hasImage == 1:
      f.write("\\hspace{0.5in}\n")
      f.write("\\includegraphics[width=2in,height=1.5in,valign=c]{"+self.imageName+"}\n")
    f.write("\\end{minipage}\n")


    f.write("\\vskip 0.20in\n\n")




  def latexAnalysisPrint(self, f):
#    f.write("\\begin{samepage} \n")
    f.write("\\item ")
    f.write(self.question + "\n")

    # find the maximum length for an answer
    mlength = 0
    for k in range(0, len(self.answer)):
      ll = len(self.answer[k])
      if (ll > mlength):
        mlength = ll 

    letters = ["(a) ","(b) ", "(c) ", "(d) ", "(e) "]
 
    f.write("\\begin{enumerate} \n")
    f.write("\\setlength{\\itemsep}{1pt} \n")
    f.write("\\setlength{\\parskip}{0pt} \n")
    f.write("\\setlength{\\parsep}{0pt}\n")

    for k in range(0, len(self.answer)):
      f.write("\item ")
      f.write( self.answer[k]  )
      f.write("\n")
    f.write("\\end{enumerate} \n")

    
    f.write("\\vskip 0.10in\n\n")






  def numberAnswers(self):
    return len(answer)

  def generateScrambled(self):

    #create an ordered list
    nlist = len(self.answer)
    tlist = range(0,nlist)
    random.shuffle(tlist)
    ltmp = list(self.answerOrder)

    for i in range(0,nlist):
      self.originalAnswer.append(self.answer[i])
 #     ltmp.append(self.answerOrder[i])
                  
    for i in range(0,nlist):
      self.answer[i] = self.originalAnswer[tlist[i]]
      self.answerOrder[i] = ltmp[tlist[i]]
    self.nanswer = tlist.index(self.originalNanswer)
    

  def generateScrambledTrimmed(self):

    # trim the list
    nlist = len(self.answer)
    tlist = range(0,nlist)
    list = random.shuffle(tlist)

    for i in range(0,nlist):
      self.answer[i] = self.originalAnswer[tlist[i]]

    self.nanswer = tlist.index(self.originalNanswer)
    

  def generateLatexKey(self, f):
    f.write("\\item ")
    answerList = ["A","B", "C", "D", "E"]
    ll = self.nanswer
    f.write(answerList[int(ll)] + "  \n")

  def generateLatexIndex(self, f):
    f.write("\\item ")
    answerList = ["A","B", "C", "D", "E"]
    ll = self.nanswer
    
    f.write(str(self.localIndex) + ", " + answerList[int(ll)] + "  \n")




