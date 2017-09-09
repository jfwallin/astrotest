


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


class testtoD2L:

  def __init__(self):

      fname = "testresults.txt"
      fname2 = "testresults-d2l.txt"
#      fname = "sample-test.txt"
#      fname2 = "sample-test-d2l.txt"
      nexam = 4
      lines = []
      newlines = []
      adjust = 0
      self.readGrade(fname,lines)
      self.processLines(lines, newlines, adjust)
      self.writeFile(fname2, nexam, newlines)

  def readGrade(self, fname, lines):

    ff = open(fname,"r")
    for line in ff:
      line = line.strip()
      lines.append(line)
    ff.close()

  def processLines(self, lines, newlines, adjust):
      for i in range(1, len(lines)):
        l = lines[i]
        val = l.split(",")
        if ( int(val[3]) > 0):
            examscore = int(val[3]) * 5 + adjust
        else:
            examscore = 0
        newlines.append(val[0]+","+str(examscore)+",#\n")
         
  def writeFile(self, fname2, nexam, newlines):
      ff = open(fname2, "w")
      ff.write("OrgDefinedID,Exam "+str(nexam)+ " Points Grade,End-of-Line Indicator\n")
      for i in range(0, len(newlines)):
        ff.write(newlines[i])
      ff.close()

if __name__ == '__main__':
  testtoD2L()
  
