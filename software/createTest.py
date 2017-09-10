
class createTest:

  def __init__(self):
    ct = 0
    self.course = "ASTR 1030 - FALL 2017 - EXAM \#7 - WALLIN"


  def startTest(self, ft):
    ft.write("\\documentclass[11pt]{article}" + "\n")
    ft.write("\\usepackage{graphicx}" + "\n")
    ft.write("\\usepackage[export]{adjustbox}" + "\n")
    ft.write("\\usepackage{multicol}" + "\n")
    ft.write("\\marginparwidth0.0in" + "\n")
    ft.write("\\evensidemargin 0.0in" + "\n")
    ft.write("\\oddsidemargin 0.0in" + "\n")
    ft.write("\\textwidth 6.67in" + "\n")
    ft.write("\\setlength{\\topmargin}{0.0in}" + "\n")
    ft.write("\\setlength{\\textheight}{9.2in}" + "\n")
    ft.write("\\pagestyle{myheadings}" + "\n")
#    ft.write("\\markboth" + "\n")
#    ft.write("{" + course + "}" + "\n")
#    ft.write("{" + course + "}" + "\n")
    ft.write("\\begin{document}" + "\n")
    ft.write("\\pagenumbering{arabic}" + "\n")

  def writeTestHeader(self, ft, version):
    ft.write("\\pagebreak \n")

    ft.write("\\setcounter{page}{1}" + "\n")
    ft.write("\\vskip 0.1in \n\n")
    ft.write("\\begin{center}" + self.course )
    #ft.write("\\bigskip" + "\n")
    ft.write("" + "\n")
    ft.write("\\vskip 0.1in \n\n")
    ft.write("\\center{\\LARGE VERSION " + str(version) + "} \n")
    ft.write("\\end{center}" + "\n")
    ft.write("Instructions (Read carefully): \n")
    ft.write("\\begin{enumerate}\n")
    ft.write("\\item ABSOLUTELY NO TALKING OR PHONE USE! \n")
    ft.write("\\item {\\bf Do not open the exam until you are directed to do so by your instructor!}\n")
    ft.write("\\item Write your name, M\#, and your clicker Device ID on the cover sheet below. \n")
    ft.write("\\item Read and sign the Honor Code Certification below.\n")
    ft.write("\\item Use your M\# for your ID on the clicker.\n")
    ft.write("\\item This is test version "+str(version) +"\n")
    ft.write("\\item Read the questions carefully. \n")
    ft.write("\\item Mark all your answers on the paper exam and THEN enter them in your clicker after you have completed the exam with a pen/pencil.\n")
    
    ft.write("\\item When you have completed the exam, turn in the exam to the LA at the front of the room and have your picture ID ready for inspection.\n")
    ft.write("\\item GOOD LUCK!!! \n")
    ft.write("\\end{enumerate}\n")
    ft.write("\\hrulefill \n")
    ft.write("\\vskip 0.1in \n\n")
    ft.write("\\begin{itemize} \\item Print your name :" + "\n")
    ft.write("\\vskip 0.25in \n\n")
    ft.write("" + "\n")


    ft.write("\\item M \# :" + "\n")
    ft.write("\\vskip 0.25in \n\n")
    ft.write("\item Clicker Device ID : " + "\n")
    ft.write("\\end{itemize} \n")
    ft.write("\\vskip 0.5in \n\n")

    ft.write("{\\bf Honor Code Certification}" + "\n")

    ft.write("\\bigskip" + "\n")
    ft.write("" + "\n")
    ft.write("I certify that I have abided by the MTSU honor code in taking this examination. The work" + "\n")
    ft.write("on this exam is my own. I have received no assistance from other persons in completing" + "\n")
    ft.write("this exam. " + "\n")
    ft.write("\\bigskip" + "\n")
    ft.write("" + "\n")
    ft.write("Signature:" + "\n")
    ft.write("" + "\n")
    ft.write("" + "\n")
    ft.write("\\pagebreak \n\n")

  def startQuestions(self, ft):
    ft.write("\\begin{enumerate}" + "\n")
    ft.write("\\setlength{\\itemsep}{1pt} \n")
    ft.write("\\setlength{\\parskip}{0pt} \n")
    ft.write("\\setlength{\\parsep}{0pt}\n")
    ft.write("\\setlength{\\multicolsep}{1pt} \n")
    ft.write("\n")

  def endQuestions(self, ft):
    ft.write("\\end{enumerate}" + "\n")

  def writeTestTrailer(self,ft):
    ft.write("\\end{document}" + "\n")



  def scrambleAnswers(self, qlist):
    for q in qlist:
      if (q.scramble == "Y"):
        q.generateScrambled()



  def writeInstructorQuestions(self,ft, qlist, offset):

    for ii in range(len(qlist)):
      qlist[ii].index = ii + 1

    qt2 = sorted(qlist, key=lambda x: x.objective)
    for q in qt2:
       print q.question       
       q.latexCompactFullPrint(ft, offset)
       print "---"


  def writeKey(self,ft, qlist):
    ct = 0
    ft.write("\\begin{multicols}{5} \n")
    for q in qlist:
      print q.question
      if (ct % 4 == 0):
        ft.write("\\vskip 0.1in \n")
      ct = ct + 1
      q.generateLatexKey(ft)
    ft.write("\\end{multicols}\n\n")

  def writeTest(self,ft, qlist):
    for q in qlist:
       q.latexCompactStudentPrint(ft)


  def tabulateTest(self,ft, qlist, questionList):
    for q in qlist:
      questionList.append(list(q.answerOrder))


  def writeTestAnalysis(self,ft, qlist):
    for q in qlist:
       q.latexAnalysisPrint(ft)


  def writeLocalIndex(self,ft, qlist):
    ct = 0
    ft.write("\\begin{multicols}{5} \n")
    for q in qlist:
      if (ct % 5 == 0):
        ft.write("\\vskip 0.1in \n")
      ct = ct + 1
      q.generateLatexIndex(ft)
    ft.write("\\end{multicols}\n\n")
