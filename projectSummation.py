import pandas as pd

df = pd.read_csv('number1.csv')

class student:

    def __init__(self, name, bengaliMark, englishMark, mathmark):
        self.name = name
        self.bengaliMark = bengaliMark
        self.englishMark = englishMark
        self.mathMark = mathmark

    def GetmyName(self):
        print("Hello my name is " + self.name)

    def GetmybengaliMark(self):
        print("Hello my bengaliMark is ",  self.bengaliMark)

    def GetmyEnglishMark(self):
        print("Hello my englishMark is ",  self.englishMark)

    def GetmymathMark(self):
        print("Hello my mathMark is ",  self.mathMark)

    def calculateTotalMarks(self):
        return self.bengaliMark+self.englishMark+self.mathMark

studentList = []

for i in range(5):
    studentList.append( student(df.Name[i],df.markBangla[i],df.markEnglish[i],df.markMath[i]))
    studentList[i].GetmyName()
    studentList[i].GetmybengaliMark()
    studentList[i].GetmyEnglishMark()
    studentList[i].GetmymathMark()
    print(studentList[i].calculateTotalMarks())




for i in range(5):
    print(studentList[i].name, studentList[i].calculateTotalMarks())


print("Program ended")
