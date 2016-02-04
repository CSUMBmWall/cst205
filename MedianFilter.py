def mediaFilter():   
    redPixelList = []
    greenPixelList = []
    bluePixelList = []   
    listMidValue = 5
    finalPicLocation = "C:\cst205\Project1Images\picFinal.png"
    finalPic = makePicture(finalPicLocation)
    finalPicPixel = getPixel(finalPic, 0,0)
    
    pictureList = []
    
    for num in range (1, 10):
      file = "C:\cst205\Project1Images\pic" + str(num) + ".png"
      picture = makePicture(file)
      pictureList.append(picture)
          
    pictureListSize = len(pictureList)
    for pixelLength in range (0, getHeight(finalPic)):
      for pixelWidth in range(0, getWidth(finalPic)):
        for num in range (0, 9):
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
        
    writePictureTo(finalPic, "C:\cst205\Project1Images\EditPic2.png")
    repaint(finalPic)
     