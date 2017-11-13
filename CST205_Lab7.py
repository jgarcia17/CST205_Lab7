#!/usr/bin/python
'''
Team 5 Hopper Pair Program
    Jose Garcia Ledesma
    Grace Alvarez

CST205-40_FA17 Lab #7
November 12th 2017
'''

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
