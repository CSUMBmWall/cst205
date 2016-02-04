def filterDriver2():
  numPics = requestNumber("How Many Pictures?")
  dateTime = requestString("What is the date and time? MM-dd-HHmm")
  filter = requestString("Filter Type? Mean or Median?")
  filter.lower()
  if filter == "median":
      medianFilter(numPics, dateTime)
  elif filter == "mean":
      meanFilter(numPics, dateTime)
      
def medianFilter(numPics, dateTime):   
  redPixelList = []
  greenPixelList = []
  bluePixelList = []   
  pictureList = []  
  listMidValue = 5
      
  for num in range (1, numPics+1):
    file = pickAFile()
    picture = makePicture(file)
    pictureList.append(picture)
  
  finalPic = makePicture(pictureList[0])
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
      setRed(finalPicPixel, redPixelList[listMidValue])
      redPixelList[:] = []
      
      greenPixelList.sort()
      setGreen(finalPicPixel, greenPixelList[listMidValue])
      greenPixelList[:] = []
    
      bluePixelList.sort()
      setBlue(finalPicPixel, bluePixelList[listMidValue])
      bluePixelList[:] = []
        
  writePictureTo(finalPic, 'C:\cst205\Project1Images\MedianEditPic" + dateTime + ".png')
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
  
  fileWriteLocation = "C:\\cst205\\Project1Images\MeanEditPic" + dateTime + ".png"    
  writePictureTo(finalPic, fileWriteLocation)
  repaint(finalPic)

    