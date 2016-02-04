def mediaFilter():   
    redPixelList = [9]
    greenPixelList = [9]
    bluePixelList = [9]   
    listMidValue = 5
    finalPicLocation = "C:\cst205\Project1Images\picFinal.png"
    finalPic = makePicture(finalPicLocation) 
    for pixelLength in range (0, getHeight(finalPic)):
		for pixelWidth in range(0, getWidth(finalPic)):
			for num in range (1, 9):
				file = "C:\cst205\Project1Images\pic" + str(num) + ".png"
				picture = makePicture(file)
				pixel = getPixel(picture, pixelWidth, pixelLength)
				redPixelList.append(getRed(pixel))
				greenPixelList.append(getGreen(pixel))
				bluePixelList.append(getBlue(pixel))        
		redPixelList.sort()
		setRed(finalPic, redPixelList[listMidValue])
		redPixelList[:] = []

		greenPixelList.sort()
		setGreen(finalPic, bluePixelList[listMidValue])
		greenPixelList[:] = []

		bluePixelList.sort()
		setBlue(finalPic, bluePixelList[listMidValue])
		bluePixelList[:] = []
		
		
for pixelWidth in range(0, 100):
referencePicPixel = getPixel(finalPic, pixelWidth,pixelLength)
setRed(finalPicPixel, getRed(referencePicPixel))
setGreen(finalPicPixel, getGreen(referencePicPixel))
setBlue(finalPicPixel, getBlue(referencePicPixel))
      
