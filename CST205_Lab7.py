#!/usr/bin/python
'''
Team 5 Hopper Pair Program
    Jose Garcia Ledesma
    Grace Alvarez

CST205-40_FA17 Lab #7
November 12th 2017
'''

#Warm-up

def drawSnowman():
  filename = pickAFile()
  pic = makePicture(filename)
  colorWhite = makeColor(255, 255, 255)
  colorBlack = makeColor(0, 0, 0)
  for x in range(1, 200):
    for y in range(0, 250):
      px = getPixel(pic, x, y)
      color = getColor(px)
      addOvalFilled(pic, 500, 230, 200, 200, colorWhite)  #Top circle
      addOvalFilled(pic, 500, 400, 200, 200, colorWhite)  #Middle Circle
      addOvalFilled(pic, 500, 570, 200, 200, colorWhite)  #Bottom Circle
      addOvalFilled(pic, 550, 270, 50, 50, colorBlack)    #Left eye Circle    
      addOvalFilled(pic, 620, 270, 50, 50, colorBlack)    #Right eye Circle
      addArcFilled(pic, 550, 300, 100, 100, 180, 180, colorBlack)  #Mouth
      addOvalFilled(pic, 590, 450, 25, 25, colorBlack)    #Button top
      addOvalFilled(pic, 590, 490, 25, 25, colorBlack)    #Button middle
      addOvalFilled(pic, 590, 530, 25, 25, colorBlack)    #Button bottom
  show(pic)
  return(pic)

#Removes green from image
def chromaKey(pic, bgpic):
  pixels = getPixels(pic)
  bgPixels = getPixels(bgpic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    if g > (b + r):
      setColor(p, getColor(getPixel(bgpic, getX(p), getY(p))))   
  
#calls chromaKey function
def makeCard():
  filename = pickAFile()
  pic = makePicture(filename)
  background = pickAFile()
  bgpic = makePicture(background)
  chromaKey(pic, bgpic)
 # repaint(pic)
  writePictureTo(pic, "C:\\Users\\Grace\\Desktop\\CSUMB\\CST205\\Module 3\\Lab 7\\ThanksgivingCard.jpg")

#Call makeCard() function
makeCard()

#Copying the image we created with the chromaKey function and using that as the background for the final card
pic = makePicture("C:\\Users\\Grace\\Desktop\\CSUMB\\CST205\\Module 3\\Lab 7\\ThanksgivingCard.jpg")
leavesPic = makePicture(pickAFile())
card = makeEmptyPicture(852, 480)

chromaKey(leavesPic, pic)  

#pastes pic 
for x in range(0, getWidth(pic)):
  for y in range(0, getHeight(pic)):
    color = getColor(getPixel(pic, x, y))
    setColor(getPixel(card, x, y), color)
#pastes leavesPic
for x in range(0, getWidth(leavesPic)):
  for y in range(0, getHeight(leavesPic)):
    color = getColor(getPixel(leavesPic, x, y))
    setColor(getPixel(card, x, y), color)
  
#adds text
fontStyle = makeStyle(serif, italic + bold, 70)
addTextWithStyle(card, 25, 450,'HAPPY THANKSGIVING!', fontStyle)

repaint (card)
writePictureTo(card, "C:\\Users\\Grace\\Desktop\\CSUMB\\CST205\\Module 3\\Lab 7\\ThanksgivingCardFinal.jpg")
