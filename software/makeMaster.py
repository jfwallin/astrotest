
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

      qfile = "all_mc_new.txt"
      qlist1 = []
      f.readMCQuestionFile(qfile, clist)
      f.processMCQuestionFile(clist, qlist1)
      print len(qlist1), len(clist)


      qdata = []
      for i in range(0,len(qlist1)):
        qdata.append(0)


      t = cTest.createTest()

      nversions = 1
      tf = open("questionMaster.tex","w")
      t.startTest(tf)
      for i in range(1, nversions + 1):
        t.writeTestHeader(tf, i)
        t.startQuestions(tf)
        t.writeInstructorQuestions(tf,qlist1)
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

