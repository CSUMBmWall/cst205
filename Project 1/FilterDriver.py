def FilterDriver(filter):   
    redPixelList = []
    greenPixelList = []
    bluePixelList = []   
    listMidValue = 5
    pixelWidth
    pixelLength
    
    finalPicLocation = "C:\cst205\Project1Images\picFinal.png"
    finalPic = makePicture(finalPicLocation)
    finalPicPixel = getPixel(finalPic, 0,0)
    x = getWidth(finalPic)
    y = getHeight(finalPic)
    pictureList = []
    
    pictureList = makePictureList(pictureList)
    for pixelLength in range (0,y):
      for pixelWidth in range(0, x):
        for num in range (0, 9):
          getPixelFromAllPics(num, redPixelList, greenPixelList, bluePixelList)
      
      finalPicPixel = getPixel(finalPic, x, y)
      
      for case in switch(filter):
        if case("median"):
          medianFilter(finalPicPixel, redPixelList, greenPixelList, bluePixelList)
          break
      
    writePictureTo(finalPic, "C:\cst205\Project1Images\EditPic2.png")
    repaint(finalPic)
    
def whichMath() 
    
def medianFilter(finalPicPixel, redPixelList, greenPixelList, bluePixelList):
  redPixelList.sort()
  setRed(finalPicPixel, redPixelList[listMidValue])
  redPixelList[:] = []
      
  greenPixelList.sort()
  setGreen(finalPicPixel, greenPixelList[listMidValue])
  greenPixelList[:] = []
      
  bluePixelList.sort()
  setBlue(finalPicPixel, bluePixelList[listMidValue])
  bluePixelList[:] = []
  
makePictureList(pictureList):
  for num in range (1, 10):
    file = "C:\cst205\Project1Images\pic" + str(num) + ".png"
    picture = makePicture(file)
    pictureList.append(picture)
    return pictureList
    
def getPixelFromAllPics(num, redPixelList, greenPixelList, bluePixelList):
  picture = pictureList[num]        
  pixel = getPixel(picture, pixelWidth, pixelLength)
  finalPicPixel = getPixel(finalPic, pixelWidth, pixelLength)
  redPixelList.append(getRed(pixel))
  greenPixelList.append(getGreen(pixel))
  bluePixelList.append(getBlue(pixel))
    
def medianFilter(num):
          
  redPixelList.sort()
  setRed(finalPicPixel, redPixelList[listMidValue])
  redPixelList[:] = []
      
  greenPixelList.sort()
  setGreen(finalPicPixel, greenPixelList[listMidValue])
  greenPixelList[:] = []
      
  bluePixelList.sort()
  setBlue(finalPicPixel, bluePixelList[listMidValue])
  bluePixelList[:] = []
     