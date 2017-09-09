

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


class makeKey:

  def __init__(self):
    keyLine = []
    countLine = []
    self.readKey(keyLine, countLine)
    f = sys.stdout


    name="Astro 1030 - Exam \#5"

    nversion = len(keyLine[0])-4

    self.writeHeader(f, name, nversion)
    qCount = len(keyLine)

    for versionCode  in range(1,nversion+2):
      self.writeVersion(f, versionCode, qCount)
      for question in range(0, len(keyLine)):
        nResponses = countLine[question][versionCode+1]
        qType = "Q"
        answer = keyLine[question][versionCode+1]
        self.writeQuestion(f, nResponses, qType, answer)


      self.writeVersionTrailer(f)
    self.writeKeyTrailer(f)

  def readKey(self,keyLine, countLine):
    ww = open("masterkey.txt","r")
    for l in ww:
        line = l.strip()
#        print line
        question = line.split(", ")
        keyLine.append(question)
#        print question, len(question)
    ww.close()

    ww = open("mastercount.txt","r")
    for l in ww:
        line = l.strip()
#        print line
        counts = line.split(", ")
        countLine.append(counts)
#        print question, len(question)
    ww.close()





  def writeHeader(self, f, testName, nVersions):
      f.write("<?xml version=\"1.0\" encoding=\"utf-8\"?> \n")
      f.write("<answerkey name=\"" + testName + "\" correctvalue=\"1\" incorrectvalue=\"0\"> \n")
      f.write("        <versions count=\"" + str(nVersions) + "\">\n")


  def writeVersion(self, f, versionCode, qCount):
      f.write("                <version code=\""+ str(versionCode) + "\">\n")
      f.write("                        <questions count=\"" + str(qCount) + "\">\n")

  def writeQuestion(self,f, nResponses,qType,answer):
      # note - only for single answer multiple choice
      f.write("                               <question type=\""+ qType + "\" maxresponse=\"" + str(nResponses) + "\" correctvalue=\"1\" incorrectvalue=\"0\">\n")
      f.write("                                        <answers count=\"1\">\n")
      f.write("                                                <answer>"  + answer + "</answer>\n")
      f.write("                                        </answers>\n")
      f.write("                                </question>\n")

  def writeVersionTrailer(self, f):
    f.write("                        </questions>\n")
    f.write("                </version>\n")

  def writeKeyTrailer(self, f):
    f.write("        </versions>\n")
    f.write("</answerkey>\n")





if __name__ == '__main__':
  makeKey()

