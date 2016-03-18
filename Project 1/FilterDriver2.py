
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

def filterDriver2():
  count = 1
  yes = true
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
      
def removeRed(picture, dateTime):
  for pixel in getPixels(picture):
    setRed(pixel, 0)
    
  writePictureTo(picture, "C:\cst205\Project1Images\Edited\RemoveRedEditPic" + dateTime + ".png")
  repaint(picture)
  
def removeGreen(picture, dateTime):
  for pixel in getPixels(picture):
    setGreen(pixel, 0)
    
  writePictureTo(picture, "C:\cst205\Project1Images\Edited\RemoveGreenEditPic" + dateTime + ".png")
  repaint(picture)
  
def removeBlue(picture, dateTime):
  for pixel in getPixels(picture):
    setBlue(pixel, 0)
    
  writePictureTo(picture, "C:\cst205\Project1Images\Edited\RemoveBlueEditPic" + dateTime + ".png")
  repaint(picture)

  
def grayScale(picture, dateTime):
  for pixel in getPixels(picture):
    newRed = getRed(pixel)*0.299
    newGreen = getGreen(pixel)*0.587
    newBlue = getBlue(pixel)* 0.114
    luminance = newRed+newGreen+newBlue
    setColor(pixel, makeColor(luminance,luminance,luminance))
  
  writePictureTo(picture, "C:\cst205\Project1Images\Edited\GrayScaleEditPic" + dateTime + ".png")
  repaint(picture)
    
def lightenPixel(picture, dateTime):
  for pixel in getPixels(picture):
    color=getColor(pixel)
    color=makeLighter(color)
    setColor(pixel, color)
  
  writePictureTo(picture, "C:\cst205\Project1Images\Edited\LightenEditPic" + dateTime + ".png")
  repaint(picture)
    
def negate(picture, dateTime):
  for px in getPixels(picture):
    red=getRed(px)
    green=getGreen(px)
    blue=getBlue(px)
    negColor=makeColor(255 - red, 255 - green, 255 - blue)
    setColor(px, negColor)
    
  writePictureTo(picture, "C:\cst205\Project1Images\Edited\NegateEditPic" + dateTime + ".png")
  repaint(picture)
      
def medianFilter(numPics, dateTime):   
  redPixelList = []
  greenPixelList = []
  bluePixelList = []   
  pictureList = []  
  midValue = 0
  
  if numPics % 2 == 0:
    midValue = int(numPics/2)
  else:
    midValue = int(numPics/2 + 1)
      
  for num in range (1, numPics+1):
    file = pickAFile()
    picture = makePicture(file)
    pictureList.append(picture)
  
  finalPic = pictureList[0]
  finalPicPixel = getPixel(finalPic, 0,0)
  
  for pixelLength in range (0, getHeight(finalPic)):
    for pixelWidth in range(0, getWidth(finalPic)):
      for num in range (0, numPics):
        picture = pictureList[num]        
        pixel = getPixel(picture, pixelWidth, pixelLength)
        finalPicPixel = getPixel(finalPic, pixelWidth, pixelLength)
        redPixelList.append(getRed(pixel))
        greenPixelList.append(getGreen(pixel))
        bluePixelList.append(getBlue(pixel))
          
      redPixelList.sort()
      setRed(finalPicPixel, redPixelList[midValue])
      redPixelList[:] = []
      
      greenPixelList.sort()
      setGreen(finalPicPixel, greenPixelList[midValue])
      greenPixelList[:] = []
    
      bluePixelList.sort()
      setBlue(finalPicPixel, bluePixelList[midValue])
      bluePixelList[:] = []
        
  writePictureTo(finalPic, "C:\cst205\Project1Images\Edited\MedianEditPic" + dateTime + ".png")
  repaint(finalPic)
    
def meanFilter(numPics, dateTime):   
  redPixelList = []
  greenPixelList = []
  bluePixelList = []   
  pictureList = []  
  
  redSum = 0
  greenSum = 0
  blueSum = 0
      
  for num in range (1, numPics+1):
    file = pickAFile()
    picture = makePicture(file)
    pictureList.append(picture)
  
  finalPic = pictureList[0]
  finalPicPixel = getPixel(finalPic, 0,0)
  
  for pixelLength in range (0, getHeight(finalPic)):
    for pixelWidth in range(0, getWidth(finalPic)):
      for num in range (0, numPics):
        picture = pictureList[num]        
        pixel = getPixel(picture, pixelWidth, pixelLength)
        finalPicPixel = getPixel(finalPic, pixelWidth, pixelLength)
        redSum += getRed(pixel) 
        redPixelList.append(getRed(pixel))
        
        greenSum += getGreen(pixel)
        greenPixelList.append(getGreen(pixel))
        
        blueSum += getBlue(pixel)
        bluePixelList.append(getBlue(pixel))
          
      mean = redSum / numPics
      setRed(finalPicPixel, mean)
      redSum = 0
      redPixelList[:] = []
      
      mean = greenSum / numPics
      setGreen(finalPicPixel, mean)
      greenSum = 0
      greenPixelList[:] = []
      
      mean = blueSum / numPics
      setBlue(finalPicPixel, mean)
      blueSum = 0
      bluePixelList[:] = []
  
  fileWriteLocation = "C:\\cst205\\Project1Images\Edited\MeanEditPic" + dateTime + ".png"    
  writePictureTo(finalPic, fileWriteLocation)
  repaint(finalPic)

    
