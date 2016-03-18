'''
Author:  Matt Wall
Date: 2/10/2016
Title: CST205 Project 1
Abstract:  Provides user interface to select image processing options:
            grayscale, lighten, negate, removeBlue, removeGreen, removeRed,
            median, and mean.  Asks for date, and then to select pic(s)


#Matt Wall, 2/8/2016  CST205 Project 114
#Median, Mean methods for pictures
#grayScale, lighten and negate methods were taken from
#http://www.cs.uregina.ca/Links/class-info/325/PythonPictures/
'''

import PIL

def getInfo():
    count = 1
    yes = True
    while(yes):
        if count > 1:
          proceed = requestString("Would you like to edit another photo? Y/N")
          if proceed == "N" or proceed == "n":
            yes = false
            break
        count += 1
        filter = requestString("Filter Type:\n" +
        "median, mean, negate, \n" +
        "lighten, grayscale, removeRed, \n" +
        "removeGreen, removeBlue")
        dateTime = requestString("What is the date and time? MM-dd-HHmm")
        filter.lower()
        if filter == "median" or filter == "mean":
          numPics = requestNumber("How Many Pictures?")
          if filter == "median":
            medianFilter(numPics, dateTime)
          else:
            meanFilter(numPics, dateTime)

        if filter != "median" and filter != "mean":
          file = pickAFile()
          picture = makePicture(file)

        if filter == "negate":
          negate(picture, dateTime)

        if filter == "lighten":
          lightenPixel(picture, dateTime)

        if filter == "grayscale":
          grayScale(picture, dateTime)

        if filter == "removeRed":
          removeRed(picture, dateTime)

        if filter == "removeGreen":
          removeGreen(picture, dateTime)

        if filter == "removeBlue":
          removeBlue(picture, dateTime)
