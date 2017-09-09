
import sys
import xml.dom.minidom
# match records program 


#import packages
#from Tkinter import *
from numpy import *
import Image, ImageDraw
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




import qb
import chapterData
import cTest  



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

      f = chapterData.chapterFile()

      qfile = "all_mc.txt" 
      qlist1 = []
      f.readMCQuestionFile(qfile, clist)
      f.processMCQuestionFile(clist, qlist1)

      qdata = []
      for i in range(0,len(qlist1)):
        qdata.append(0)        
      self.readQList(qdata)


      # make the final list
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
      aux = 0
      if (aux == 1):
        qlistAux = []
        clistAux = []
        fAux = chapterData.chapterFile()

        qfileAux = "aux_mc.txt" 
        qlistAux1 = []
        f.readMCQuestionFile(qfileAux, clistAux)
        f.processMCQuestionFile(clistAux, qlistAux1)

        for jj in range(0, len(qlistAux1)):
          qaux = qlistAux1[jj]
          qlist2.append(qaux)
          qlist2[ct].globalIndex = qaux
          qlist2[ct].localIndex = ct + 1
          ct = ct + 1
          
      ############################
      for q in qlist2:
        q.nanswer = int(q.nanswer)
        q.originalNanswer = int(q.nanswer)

      qlist3 = qlist2
      ############################
      #  start writing the 5 version of the test out
      testList = []
      nversions = 5
      for i in range(0, nversions + 1):
        t = cTest.createTest()
        tname = "SUMMARY"+str(i) + ".tex"
        tf = open(tname,"w")

        t.startTest(tf)
        t.writeTestHeader(tf, i)
        t.startQuestions(tf)
        t.writeTestAnalysis(tf,qlist2)

        questionList = []
        t.tabulateTest(tf, qlist2, questionList)
        testList.append(list(questionList))        
        t.endQuestions(tf)

        
        #        t.startQuestions(tf)
        #        t.writeKey(tf,qlist2)
        #        t.endQuestions(tf)

      

        #      t.startQuestions(tf)
        #      t.writeLocalIndex(tf,qlist2)
        #      t.endQuestions(tf)
        
        #      localCount = []
        #      localKey = []
        #      localIndex = []
        #      for q in qlist2:
        #        answerList = ["A","B", "C", "D", "E"]
        #        ll = q.nanswer
        #        localKey.append(answerList[int(ll)] )
        #        localIndex.append(q.localIndex)
        #        localCount.append(len(q.answer))
        #      masterKey.append(localKey)
        #      masterIndex.append(localIndex)
        #      masterCount.append(localCount)


        t.scrambleAnswers(qlist2)
        random.shuffle(qlist2) 
        t.writeTestTrailer(tf)
        tf.close()
        
      print "----"
      print testList[0]
      print"====="
      print testList[1]

      # generate the look up list for questions, the correlation matrix, and the full set of keys
#      self.generateReports(qlist2, qdata, masterKey, masterIndex, masterCount, nversions)
      
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
      ii = int(line)
      qdata[ii] = 1

  def generateReports(self, qlist2, masterList, masterKey, masterIndex, masterCount, nversions):
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




if __name__ == '__main__':
  reformat()
  
