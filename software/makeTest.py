
import sys
import xml.dom.minidom
# match records program


#import packages
#from Tkinter import *
from numpy import *
#import Image, ImageDraw
import math
import urllib
#import Tkinter, ImageTk
import sys
import time
import os
import glob
import string
import re
import random


keyString = "Answer:"
KEY = 100
DIFF = 200
diffString = "Diff:"
SECTION = 300
sectionString = "Section Ref:"
QUESTION = 500
mcString = ["A) ", "B) ", "C) ", "D) ", "E) "]
mcOFFSET = 1000


questionGroup = ["True/False Questions","Multiple-Choice Questions","Fill-in-the-Blank Questions","Short Answer Questions","Essay Questions"]



# testbank format
# header
#Astronomy: A Beginner's Guide to the Universe, 6e (Chaisson/McMillan)
#Chapter 0   Charting the Heavens: The Foundations of Astronomy




import questionblock as qb
import chapterData
import createTest as cTest



class reformat:


  def __init__(self):

      random.seed(2)
      cf = []
      qlist = []
      clist = []

      iNotate = []
      iKey = []
      iSection = []
      iDiff = []

      # read in and parse the test questions from the test bank
      f = chapterData.chapterFile()

      qfile = "all_mc_new.txt"
      qlist1 = []
      sectionData = []
      f.readMCQuestionFile(qfile, clist)
      f.processMCQuestionFile(clist, qlist1, sectionData)
  
      qdata = []
      for i in range(0,len(qlist1)):
        qdata.append(0)

      self.readQList(qdata)
      
      print sectionData




# block
      # make the final list of questions
      ct = 0
      qlist2 = []
      masterKey = []
      masterIndex = []
      masterCount = []
      masterIndex = []
      for i in range(0, len(qlist1)):
        if (qdata[i] == 1):
          qlist2.append(qlist1[i-1])
          qlist2[ct].globalIndex = i
          qlist2[ct].localIndex = ct + 1
          ct = ct + 1


      ###########################

#      cf = []
      qlistAux = []
      clistAux = []

      # aux = 0
      # # if there are addiitonal non-testbank questions, you can add them in an aux_mc.txt file.
      # # every question from this file will be included in the test along with the questions
      # # selected from the test bank
      # if (aux == 1):
      #   fAux = chapterData.chapterFile()

      #   qfileAux = "aux_mc.txt"
      #   qlistAux1 = []
      #   f.readMCQuestionFile(qfileAux, clistAux)
      #   f.processMCQuestionFile(clistAux, qlistAux1)

      #   for jj in range(0, len(qlistAux1)):
      #     qaux = qlistAux1[jj]
      #     qlist2.append(qaux)
      #     qlist2[ct].globalIndex = qaux
      #     qlist2[ct].localIndex = ct + 1
      #     ct = ct + 1



# block
      # set the number of the answer and the original answers before processing
      for q in qlist2:
        q.nanswer = int(q.nanswer)
        q.originalNanswer = int(q.nanswer)
      

      testList = []
      nversions = 4
      for i in range(0, nversions + 1):
        t = cTest.createTest()
        tname = "TEST"+str(i) + ".tex"
        tf = open(tname,"w")

        # write the body of the test
        t.startTest(tf)
        t.writeTestHeader(tf, i)
        t.startQuestions(tf)
# block
#        t.writeTest(tf,qlist2)

        for j in range(len(sectionData)):
          istart = sectionData[j][1]
          iend = sectionData[j][2]

          tf.write("\\pagebreak \n")
          tf.write("\\begin{minipage}{\\textwidth} \n")
          tf.write("\\begin{minipage}{\\textwidth} \n")
          tf.write("\\bigskip SECTION = " + str(j) + "\n")
          tf.write("\\end{minipage}\n")
          tf.write("\\end{minipage}\n")
          #t.writeTest(tf,qlist1[istart:iend])
          t.writeTest(tf,qlist2)

        t.endQuestions(tf)

        # question analysis
        questionList = []
        t.tabulateTest(tf, qlist2, questionList)
        testList.append(list(questionList))

        t.startQuestions(tf)
        t.writeKey(tf,qlist2)
        t.endQuestions(tf)

        t.startQuestions(tf)
        t.writeLocalIndex(tf,qlist2)
        t.endQuestions(tf)

        localCount = []
        localKey = []
        localIndex = []
        for q in qlist2:
          answerList = ["A","B", "C", "D", "E"]
          ll = q.nanswer
          localKey.append(answerList[int(ll)] )
          localIndex.append(q.localIndex)
          localCount.append(len(q.answer))
        masterKey.append(localKey)
        masterIndex.append(localIndex)
        masterCount.append(localCount)

        t.scrambleAnswers(qlist2)
        random.shuffle(qlist2)
        t.writeTestTrailer(tf)
        tf.close()

      # generate the look up list for questions, the correlation matrix, and the full set of keys
      self.generateReports(qlist2, qdata, masterKey, masterIndex, masterCount, testList, nversions)

  def showFiles(self, cf):

      # read the chapter test file list and parse them
      path = './'
      for infile in glob.glob( os.path.join(path, '*') ):
          ss = []
          ss = infile.split("/")
          ok =  string.find(ss[1],"test")
          if (ok > 0):
              cf.append(infile)

      for i in range(0, len(cf)):
          print i, ")  ", cf[i]


  def readQList(self, qdata):
    qf = open("qfile","r")
    for line in qf:
      line = line.strip()
      print line
      ii = int(line)
      qdata[ii] = 1

  def generateReports(self, qlist2, masterList, masterKey, masterIndex, masterCount, testList, nversions):
    ml = open("masterlist.txt","w")
    ct = 0
    for i in range(0, len(masterList)):
      if (masterList[i] == 1):
        ml.write(str(ct + 1) + ", " + str(i) + "\n")
        ct = ct +1
    ml.close()

    mk = open("masterkey.txt","w")
    for j in range(0, len(masterKey[0])):
      mk.write(str(j+1) + ", ")
      for i in range(0,nversions+1):
        mk.write(masterKey[i][j] + ", ")
      mk.write("# \n")
    mk.close()

    mk = open("mastercount.txt","w")
    for j in range(0, len(masterKey[0])):
      nanswers = len(qlist2[j].answer)
      mk.write(str(j+1) + ", " )
      for i in range(0,nversions+1):
        mk.write(str(masterCount[i][j]) + ", ")
      mk.write("# \n")
    mk.close()

    mi = open("masterindex.txt","w")
    for j in range(0, len(masterIndex[0])):
      mi.write(str(j+1) + ", ")
      for i in range(0,nversions+1):
        mi.write(str(masterIndex[i][j]) + ", ")
      mi.write("# \n")
    mi.close()

    mc = open("mastercorrelation.txt","w")
    for j in range(0, len(testList)):
      for k in range(0, len(testList[j])):
        mc.write(str(j) + ", " + str(k+1) + "; "+ str(testList[j][k][0]))
        for l in range(1, len(testList[j][k])):
          mc.write(", " + str(testList[j][k][l]))
        mc.write( "; " + str(masterIndex[j][k]) + ", " + masterKey[j][k])
        mc.write("\n")
    mc.close()



if __name__ == '__main__':
  reformat()

