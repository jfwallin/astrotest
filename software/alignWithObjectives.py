
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


class parseObjectives:

  def __init__(self):

    fn = "../software/objectiveList-2016.csv"
    self.objectiveDictionary = self.readObjectives(fn)
#    self.questionFrequency()
    self.questionFrequency()

  def readObjectives(self, fn):

    ll = {}
#    print fn
    f = open(fn,"r")
    for l in f:
      cl = l.find(",")
      key = l[0:cl]
      val = l[cl+1:].strip()
      #print key, val
      ll[ float(key)] = val

    f.close()
    ll[0] = "Constellations"
    ll[9999] = "Other questions"
    return ll


  def questionFrequency(self):

    self.questionDictionary = {}
    for infile in glob.glob( os.path.join(".", 'qfile.t*') ):
      usedQuestions = []
      f = open(infile,"r")
      for l in f:
        qnumber = int(l.strip())

        if  qnumber in self.questionDictionary:
          self.questionDictionary[qnumber] += 1
        else:
          self.questionDictionary[qnumber] = 1

      f.close()
#    print self.questionDictionary
    
      




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


      p = parseObjectives()
      print p.objectiveDictionary[11.1]
      



      # read in the question file
      f = chapterData.chapterFile()
      qfile = "all_mc_new.txt"
      qlist1 = []
      f.readMCQuestionFile(qfile, clist)
      f.processMCQuestionFile(clist, qlist1)
      #print len(qlist1), len(clist)


      # initialize the qdata array
      qdata = []
      for i in range(0,len(qlist1)):
        qdata.append(0)


      # go through the question list qlist1, and create a list of the
      # unique objectives in the list
      objList = []
      uniqueObjList = []
      for q in qlist1:
        obj = q.objective
        #######print obj, q.question
        if obj.find("Z") > -1:
          objVal = 9999
        elif obj.find("C") > -1:
          objVal = 0
        else:
          try:
            objVal = float(obj)
          except ValueError:
            objVal = -1
            print "error for ",q.question
        #print objVal, float(objVal)
#        if float(objVal) == 1.0:
#          print "quack", q.question
        objList.append([float(objVal), q.question])
        uniqueObjList.append(float(objVal))

      uniqueObjList = list(sorted(set(uniqueObjList)))
      print uniqueObjList


      # loop through all of the unique objectives and print out the questions that
      # match them in a formated way
      lastObjective = -1
      for objective in uniqueObjList:
        if objective != lastObjective:
          print "==================================================="
          print "obj = ", objective
          print "=======", objective, p.objectiveDictionary[objective]
          lastObjective = objective

          for iq in range(len(objList)):
            q = objList[iq]
            if q[0] == objective:
              if iq in p.questionDictionary:
                nt = p.questionDictionary[iq]
                ns = ""
                for k in range(nt):
                  ns = ns + "*"
              else:
                ns = ""

              # change the lenght of ns so it is alway 7 characters
              lns = len(ns)
              for i in range(7 - lns):
                ns = " " + ns

                
              
              ss = qlist1[iq].source
#              print iq, ss
              if ss == "homework":
                ss1 = " (hw) "
              elif ss == "testbank":
                ss1 = " (tb) "
              elif ss == "clicker":
                ss1 = " (cl) "
              elif ss == "pretest":
                ss1 = " (pt) "
              else:
                ss1 = " (??) "


              s = str(ns) +  ss1 + str(iq+1) + ": " + q[1]
              print s
#              print ns, iq+1,  q[1]
#              print ">",qlist1[iq].question

        

      exit()


      t = cTest.createTest()

      nversions = 1
      tf = open("questionMaster.tex","w")
      t.startTest(tf)
      for i in range(1, nversions + 1):
        t.writeTestHeader(tf, i)
        t.startQuestions(tf)
        t.writeInstructorQuestions(tf,qlist1)
        t.endQuestions(tf)

        # write the key
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

