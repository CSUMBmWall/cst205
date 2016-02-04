def mediaFilter2():
  redPixelList = []
  greenPixelList = []
  bluePixelList = []   
  listMidValue = 1
  modifiedPicLocation = "C:\cst205\Project1Images\pic5.png"
  modifiedPic = makePicture(modifiedPicLocation)
  modifiedPicPixel = getPixel(modifiedPic, 0,0)
    
  referencePicLocation = "C:\cst205\Project1Images\pic6.png"
  referencePic = makePicture(referencePicLocation)
  for pixelLength in range (175, 500):
    for pixelWidth in range(0, 100):
      referencePicPixel = getPixel(referencePic, pixelWidth, pixelLength)
      modifiedPicPixel = getPixel(modifiedPic, pixelWidth, pixelLength)
      setRed(modifiedPicPixel, getRed(referencePicPixel))
      setGreen(modifiedPicPixel, getGreen(referencePicPixel))
      setBlue(modifiedPicPixel, getBlue(referencePicPixel))
      
  #for pixelLength in range(200, 500):
    #for pixelWidth in range(500, getWidth(modifiedPic)):
      #referencePicPixel = getPixel(referencePic, pixelWidth, pixelLength)
      #modifiedPicPixel = getPixel(modifiedPic, pixelWidth, pixelLength)
      #redAvg =  (getRed(referencePicPixel) + getRed(modifiedPicPixel))/2
      #setRed(modifiedPicPixel, redAvg)
    
      #greenAvg =  (getGreen(referencePicPixel) + getGreen(modifiedPicPixel))/2
      #setGreen(modifiedPicPixel, greenAvg)
    
      #blueAvg =  (getBlue(referencePicPixel) + getBlue(modifiedPicPixel))/2
      #setBlue(modifiedPicPixel, blueAvg)
    
  writePictureTo(modifiedPic, "C:\cst205\Project1Images\EditPic2.png")
  repaint(modifiedPic)
  