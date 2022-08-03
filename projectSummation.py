import string
from unicodedata import name
import pandas as pd

df = pd.read_csv('number1.csv')

class student:

    def __init__(self, name, bengaliMark, englishMark, mathmark):
        self.name = name
        self.bengaliMark = bengaliMark
        self.englishMark = englishMark
        self.mathMark = mathmark

    def myName(self):
        print("Hello my name is " + self.name)

    def mybengaliMark(self):
        print("Hello my bengaliMark is ",  self.bengaliMark)

    def myenglishMark(self):
        print("Hello my englishMark is ",  self.englishMark)

    def mymathMark(self):
        print("Hello my mathMark is ",  self.mathMark)

    def totalMarks(self):
        BANGLAmark = float(self.bengaliMark)
        ENGLISHmark = float(self.englishMark)
        MATHmark = float(self.mathMark)
        total = BANGLAmark+ENGLISHmark+MATHmark
        return total

studentList = []

for i in range(5):
    studentList.append( student(df.Name[i],df.markBangla[i],df.markEnglish[i],df.markMath[i]))
    studentList[i].myName()
    studentList[i].mybengaliMark()
    studentList[i].myenglishMark()
    studentList[i].mymathMark()
    print(studentList[i].totalMarks())

for i in range(5):
    print(studentList[i].name, studentList[i].totalMarks())


print("Program ended")
