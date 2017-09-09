
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

class getClickerQuestions:
    
  def __init__(self):
    flist = [] 
    self.grabFiles(flist)
    for f in flist:
#      print f
      self.xmlget(f)

  def grabFiles(self, flist):
    # read the lectures clicker file list and parse the
    path = 'tpq/'
    for infile in glob.glob( os.path.join(path, '*') ):
      ss = []
      ss = infile.split("/")
      ok =  string.find(ss[1],"tpq")
      
      if (ok > 0):
        flist.append(infile)
          
#      print " "

  def xmlget(self, fname):

    ff = sys.stdout
    xmldoc = xml.dom.minidom.parse(fname)
    slides = xmldoc.getElementsByTagName("slide")
#    print "slide ", len(slides)
    for islide in range(0, len(slides)):
      ff.write("NEW\n")
      slide = slides[islide]

      questionText = []
      questionBlock = slide.getElementsByTagName("question")[0]
      self.handleQuestion(questionBlock, questionText)
      t = questionText[0]
      
      ff.write("question="+ t.encode('ascii','ignore')+"\n")

      answerBlock = slide.getElementsByTagName("answer")
      answerList = []
      self.handleAnswers(answerBlock, answerList)
      for a in answerList:
        ff.write("answer="+ a.encode('ascii','ignore')+"\n")
#      print answerList

      ff.write("key=\n")
      ff.write("chapter=-1\n")
      ff.write("index="+str(islide)+"\n")
      ff.write("difficulty=0\n")
      ff.write("scramble=Y\n")
      ff.write("type=MC\n")


      
#      ltmp = question
#      question = self.getText(questionBlock.childNodes)
#      print question
#      answers = ltmp.getElementsByTagName("answer")
#      print "len = ", len(answers)
#      for j in range(0, len(answers)):
#        ktmp = answers[i]
#        print self.getText(ktmp.childNodes)

#      answerList.append(letter)



  def handleAnswers(self,answers, answerList):
    for answer in answers:
     # answerText = ""
     # self.handleAnswer(answer, answerText)
      answerText =  self.getText(answer.childNodes)
      answerList.append(answerText)

  def handleQuestion(self,question,questionText):
    qt =  self.getText(question.childNodes)
    questionText.append(qt)
    
#########  
  def getText(self, nodelist):
    rc = []
    for node in nodelist:
      if node.nodeType == node.TEXT_NODE:
        rc.append(node.data)
    return ''.join(rc)



if __name__ == '__main__':
  getClickerQuestions()
  
