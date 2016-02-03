def medianFilter():   
    redPixelList = [9]
    greenPixelList = [9]
    bluePixelList = [9]   
    listMidValue = 5
    finalPicLocation = "C:\cst\CST205\Project1Images\pic10.png"
    finalPic = makePicture(finalPicLocation)
    for pixelLength in range (0, getHeight(finalPic)):