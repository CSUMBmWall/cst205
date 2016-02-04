class PicData(numPics, dateTime):
  numPics
  dateTime
  def __init__(self):
    self.numPics = numPics
    self.dateTime = dateTime

    redPixelList = []
    greenPixelList = []
    bluePixelList = []  		
	
def filterDriver2():
  numPics = requestNumber("How Many Pictures?")
  dateTime = requestString("What is the date and time? MM-dd-HHmm")
  picData = PicData(numPics, dateTime)
  filter = requestString("Filter Type? Mean or Median?")
  filter.lower()
  if filter == "median":
      medianFilter(picData)
  elif filter == "mean":
      meanFilter(picData)
      
def medianFilter(picData):   
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
        picData.redPixelList.append(getRed(pixel))
        picData.greenPixelList.append(getGreen(pixel))
        picData.bluePixelList.append(getBlue(pixel))
          
      picData.redPixelList.sort()
      setRed(finalPicPixel, picData.redPixelList[midValue(picData)])
      redPixelList[:] = []
      
      picData.greenPixelList.sort()
      setGreen(finalPicPixel, picData.greenPixelList[midValue(picData)])
      greenPixelList[:] = []
    
      picData.bluePixelList.sort()
      setBlue(finalPicPixel, picData.bluePixelList[midValue(picData)])
      picData.bluePixelList[:] = []
        
  writePictureTo(finalPic, 'C:\cst205\Project1Images\MedianEditPic" + dateTime + ".png')
  repaint(finalPic)
  
def midValue(picData):
	if picData.numPics % 2 == 0:
		return picData.numPics/2
	return picData.numPics/2 + 1
    
def meanFilter(picData):   
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
        picData.redPixelList.append(getRed(pixel))
        
        greenSum += getGreen(pixel)
        picData.greenPixelList.append(getGreen(pixel))
        
        blueSum += getBlue(pixel)
        picData.bluePixelList.append(getBlue(pixel))
          
      mean = redSum / numPics
      setRed(finalPicPixel, mean)
      redSum = 0
      picData.redPixelList[:] = []
      
      mean = greenSum / numPics
      setGreen(finalPicPixel, mean)
      greenSum = 0
      picData.greenPixelList[:] = []
      
      mean = blueSum / numPics
      setBlue(finalPicPixel, mean)
      blueSum = 0
      picData.bluePixelList[:] = []
  
  fileWriteLocation = "C:\\cst205\\Project1Images\MeanEditPic" + dateTime + ".png"    
  writePictureTo(finalPic, fileWriteLocation)
  repaint(finalPic)