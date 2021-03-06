import sys
import xml.dom.minidom
# match records program 


#import packages
#from Tkinter import *
from numpy import *
import Image, ImageDraw
import math
import urllib
import Tkinter, ImageTk
import sys
import time
import os
import glob
import string

import studentTestRecord

class analysis:

 def __init__(self):
   print "Duekc"
   cmatrix = []
   amatrix = []
   records = []
   summaryPoints = []
   summaryPossible = []
   self.grabFiles(cmatrix, amatrix, records)

   print "@#$@#$@#"
   for i in range(0, len(cmatrix)):
       summaryPoints.append(0)
       summaryPossible.append(0)

   for s in range(0, len(records)):
       
     studentPoints = []
     studentPossible = []
     record = records[s]
     if (record.version != ""):   
         version = int(record.version)
     else:
         version = 0
     self.gradeStudent(version, amatrix, record, studentPoints, studentPossible)
     
     score = []
     possible = []
     self.calcScore(studentPoints, studentPossible, score, possible)

     # get the order of the questions
     order = []
     for i in range(len(cmatrix)):
         aa = cmatrix[i]
         ii = int(aa[version])
         order.append( ii)
         
     for i in range(len(order)):
         ii = order[i] -1
         summaryPoints[ii] = summaryPoints[ii] + studentPoints[i]
         summaryPossible[ii] = summaryPossible[ii] + studentPossible[i]


   print " "
   print " "
   print " "
   print "SUMMARY "
   for i in range(0, len(summaryPoints)):

       val = float(summaryPoints[i]) / float(summaryPossible[i])
#       if (val < 0.5):
       if (val < 1.1):
           valp = float(  int(val * 1000))/1000.
           ns = int(val * 10) + 1
           sys.stdout.write(str(i+1) + ",  " +  str(valp) + ", ")
           for ii in range(0, ns):
               sys.stdout.write("*")
           sys.stdout.write("\n")
   print summaryPoints
   print summaryPossible

   
 def calcScore(self, studentPoints, studentPossible, score, possible):
   score.append(0)
   possible.append(0)
   for p in range(0, len(studentPoints)):
     score[0] = score[0] + studentPoints[p]
     possible[0] = possible[0] + studentPossible[p]

 def gradeStudent(self, version, amatrix, record, studentPoints, studentPossible):
  answers = record.testString
  for ii in range(0, len(answers)):
    cvalue = string.find(amatrix[ii][version],answers[ii])
    if (cvalue > -1):
      studentPoints.append(1)
    else:
      studentPoints.append(0)

    valid = string.find(answers[ii], "-")
    if (valid == -1):
      studentPossible.append(1)
    else:
      studentPossible.append(0)

      

 def grabFiles(self, cmatrix, amatrix, records):
     # read the index file for the quesiton order
   fname = "masterindex.txt"
   self.readIndex(fname, cmatrix)

   # read the index file for the quesiton order
   fname = "masterkey.txt"
   self.readIndex(fname, amatrix)

   # read the student answers
   fname = "Individual Results.csv"
   lines = []
   self.readFile(fname, lines)
   self.procLines(lines, records)
  

 def readFile(self, fname, lines):
   ff = open(fname,"r")
   for l in ff:
     l = l.strip()
     lines.append(l)
   ff.close()

 def procLines(self, lines, records):
   kk = -1
   for ii in range(0, len(lines)):
     ok = string.find(lines[ii], "Device")
#     print ii, ok, lines[ii], 
     if (ok > -1):
       kk = ii

   if (kk > -1):
     for ii in range(kk+1, len(lines)):
       aa = studentTestRecord(lines[ii])
       print ii, len(records), lines[ii]
       records.append(aa)
   else:
      print "error!"
      

 def readIndex(self, file, cmatrix):
   fc = open(file, "r")
   for line in fc:
     l = line.strip()
     val = l.split(",")
     # for 5 versions of the test
     cmatrix.append(val[1:7])
   fc.close()
