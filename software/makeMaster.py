
import sys
import xml.dom.minidom
# match records program


#import packages
from numpy import *
import math
import urllib
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

      f = chapterData.chapterFile()

      qfile = "all_mc_new.txt"
      qlist1 = []
      sectionData = []
      f.readMCQuestionFile(qfile, clist)
      f.processMCQuestionFile(clist, qlist1, sectionData)
      print len(qlist1), len(clist)


      qdata = []
      for i in range(0,len(qlist1)):
        qdata.append(0)


      t = cTest.createTest()

      nversions = 1
      tf = open("questionMaster1.tex","w")
      t.startTest(tf)
      for i in range(1, nversions + 1):
        t.writeTestHeader(tf, i)
        t.startQuestions(tf)
        for j in range(len(sectionData)):
          istart = sectionData[j][1]
          iend = sectionData[j][2]

          tf.write("\\pagebreak \n")
          tf.write("\\begin{minipage}{\\textwidth} \n")
          tf.write("\\begin{minipage}{\\textwidth} \n")
          tf.write("\\bigskip SECTION = " + str(j) + "\n")
          tf.write("\\end{minipage}\n")
          tf.write("\\end{minipage}\n")
          t.writeInstructorQuestions(tf,qlist1[istart:iend], istart)
        t.endQuestions(tf)

        t.startQuestions(tf)
        t.writeKey(tf,qlist1)
        t.endQuestions(tf)


      t.writeTestTrailer(tf)
      tf.close()


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


if __name__ == '__main__':
  reformat()
  print "DONE"
