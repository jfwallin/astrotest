
1) Create a master test.
python ../software/makeMaster.py 

This creates a file called questionMaster.tex.

This is a complete latex formatted version of the test bank.

2) Create verison of the test master that is sorted by objective number. This just includes a one-line summary of the text of the question.
python ../software/alignWithObjectives.py > questionlist.txt

3) Edit the questionlist.txt file.  Add an "x" in the first column for every question that you want to include in the exam.

Describe the composition, orbits, and characteristics of the Kuiper belt objects and how they were discovered.
[0.0, 1.1, 1.2, 1.4, 2.2, 2.3, 2.4, 2.5, 2.6, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 5.2, 5.3, 5.4, 9999.0]
===================================================
obj =  0.0
======= 0.0 Constellations
     ** (tb) 2: In {\bf Figure 1} at the back of the test, which letter is closest to the Polaris?
  ***** (tb) 3: In {\bf Figure 1} at the back of the test, which letter is closest to the star Thuban?
      * (tb) 4: The star Thuban:
   **** (tb) 5: In {\bf Figure 1} at the back of the test, which letter is closest to the constellation of Draco?
x      * (tb) 6: In {\bf Figure 1} at the back of the test, which letter is closest to the constellation of  Cassiopeia?
x      * (tb) 47: In figure 1 at the back of the test, which letter is closest to the constellation of Cepheus?
        (tb) 48: In figure 1 at the back of the test, which letter is closest to the constellation of Ursa Major?
      * (tb) 49: In figure 1 at the back of the test, which letter is closest to the constellation of Ursa Minor?
===================================================
obj =  1.1
======= 1.1 Explain how locations are described on Earth using geographic regions, latitude/longitude, and local directions.
        (tb) 76: Latitude and longitude measure:
x        (cl) 170: Latitude and longitude measure:
===================================================
obj =  1.2
======= 1.2 Summarize what constellations are and describe how they are used to identify patterns of stars and to divide the sky into “geographic” regions.
      * (tb) 108: How many constellations cover surface of the Celestial Sphere?
        (hw) 115: The stars in a constellation are physically close to one another.
        (hw) 122: The celestial sphere is divided into 88 modern constellations.
x        (hw) 131: Constellations are close clusters of stars, all at about the same distance from the Sun.
...


4) Create a textfile that lists the question ID numbers for everything you checked in the questionlist.txt file.  You could also create this directly from the questionMaster.txt file.

python ../software/questiontoqlist.py  > qfile


5) Create the tests:
python ../software/makeTest.py 

This creates TEST0.tex to TEST4.tex

TEST0 is the unscrambled version of the quesitons and the answers.  The rest of the tests are scrambled.

6) Create the answer key file.  The format (tky) is basicaly a XML format for text keys, and compatable with the clicker software.
/python ../software/makeClickerKey.py > test1.tky




SOFTWARE
alignWithObjectives.py
analysis.py
cTest.py
chapterData.py
clickerQuestions.py
makeClickerKey.py
makeKey.py
makeMaster.py
makeTest.py
masterTest.py
newObjectives.py
newnumber.py
qb.py
questiontoqlist.py


TEST0
all_mc_new.txt
images
objectiveList-2016.csv
qfile
qfile.t1_f2012
qfile.t1_f2013
qfile.t1_f2014
qfile.t1_f2015
qfile.t1_f2016
qfile.t1_s2015
qfile.t1_s2016
