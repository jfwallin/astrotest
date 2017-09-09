
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


test = []
class makeKey:

  def __init__(self):
      self.readKey()
      f = sys.stdout
      name="Astro 1030 - Exam 5"
      nversion = 5
      self.writeHeader(f, name, nversion)

  def readKey(self):
    test = []
    ww = open("masterkey.txt","r")
    for l in ww:
        line = l.strip()
        print line
        question = line.split(", ")
        test.append(question)
    ww.close()

  def writeHeader(self, f, name, nversion):
      f.write("<?xml version=\"1.0\" encoding=\"utf-8\"?> \n")
      f.write("<answerkey name=\"" + name + "\" correctvalue=\"1\" incorrectvalue=\"0\"> \n")
      f.write("        <versions count=\"" + str(nversion) + "\">\n")

      f.write("                <version code=\"1\">\n")
      f.write("                        <questions count=\"50\">\n")
      f.write("                               <question type=\"Q\" maxresponse=\"5\" correctvalue=\"1\" incorrectvalue=\"0\">\n")
      f.write("                                        <answers count=\"1\">\n")
      f.write("                                                <answer>E</answer>\n")
      f.write("                                        </answers>\n")
      f.write("                                </question>\n")






if __name__ == '__main__':
  makeKey()

