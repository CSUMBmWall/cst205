pics = []
for x in range (1,10):
  filePics = "c:/cst205/Project1Images/pic1.png"
  finalPic = makePicture(filePics)
  pics.append(finalPic)
  #pixel = getPixel(pics[0],0,0) 
  #red = getRed(pixel)

width = getWidth(pics[0])
height = getHeight (pics[0])

makeRed = []
makeBlue = []
makeGreen = []


final = makeEmptyPicture(width, height)


for x in range (0,width):
  for y in range (0,height):
    for i in pics:
      pixel = getPixel(i, x, y)
     
      red = getRed(pixel)
      makeRed.append(red)
    
      green = getGreen(pixel)
      makeGreen.append(green)
   
      blue = getBlue(pixel)
      makeBlue.append(blue)
    
    makeRed.sort()
    makeGreen.sort()
    makeBlue.sort()

   
    pixel = getPixel(final, x, y)
    newColor = makeColor(makeRed[5], makeGreen[5], makeBlue[5])
    setColor(pixel, newColor)
  
    makeRed[:] = []
    makeGreen[:] = []
    makeBlue[:] = [] 
    
    

print hello 
    
picName = requestString("Name the picture:")
writePictureTo(final, "/Users/Meya/Desktop/205pics/" +picName+ ".png")

repaint(final)