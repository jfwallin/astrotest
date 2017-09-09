
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

      ilecture = -1
      self.showFiles(cf)
#      ilecture = int(raw_input("Enter the file you wish to select :"))      

      for ilecture in range(0,len(cf)):
        chapter = cf[ilecture][2:4]
        clist = []
        iNotate = []
        f.readFile(cf[ilecture],ilecture,clist)
        print ilecture, len(clist)
        f.findQuestionBlocks(iNotate, clist)
        f.processMCQuestions(chapter, iNotate, clist, qlist)
        f.processTFQuestions(chapter, iNotate, clist, qlist)

      #  newname = chapter + "_" + "mc.txt"
      qfile = "all_mc.txt" 
      f.writeMCQuestionFile(qfile, qlist)





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



if __name__ == '__main__':
  reformat()
  
