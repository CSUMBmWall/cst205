def medianFilter():   
    redPixelList = [9]
    greenPixelList = [9]
    bluePixelList = [9]   
    listMidValue = 5
    finalPicLocation = "C:\cst\CST205\Project1Images\pic10.png"
    finalPic = makePicture(finalPicLocation)
    for pixelLength in range (0, getLength(pict)):
      for pixelWidth in range(0,getWidth(pict)):
        for num in range (1, 9):
        file = "C:\cst\CST205\Project1Images\pic" + num + ".png"
        picture = makePicture(file)
        pixel = getPixel(picture, pixelWidth, pixelLength)
        redPixelList.append(getRed(pixel))
        greenPixelList.append(getGreen(pixel))
        bluePixelList.append(getBlue(pixel))
        
      redPixelList.sort()
      setRed(finalPic, redPixelList[listMidValue]
      redPixelList[:] = []
      
      greenPixelList.sort()
      setGreen(finalPic, bluePixelList[listMidValue]
      greenPixelList[:] = []
      
      bluePixelList.sort()
      setBlue(finalPic, bluePixelList[listMidValue]
      bluePixelList[:] = []
      
      
        
        
        
      
      