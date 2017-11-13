#!/usr/bin/python
'''
Team 5 Hopper Pair Program
    Jose Garcia Ledesma
    Grace Alvarez

CST205-40_FA17 Lab #7
November 12th 2017
'''

#Thanksgiving Card
def chromaKey(pic, bgpic):
  pixels = getPixels(pic)
  bgPixels = getPixels(bgpic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    if g > (b + r):
      setColor(p, getColor(getPixel(bgpic, getX(p), getY(p))))   
  
  #add text
  fontStyle = makeStyle(serif, italic + bold, 70)
  addTextWithStyle(pic, 25, 400,'HAPPY THANKSGIVING!', fontStyle)
  
def makeCard():
  #Call Thanksgiving Card
  filename = pickAFile()
  pic = makePicture(filename)
  background = pickAFile()
  bgpic = makePicture(background)
  chromaKey(pic, bgpic)
  repaint(pic)
  writePictureTo(pic, "C:\\Users\\Grace\\Desktop\\CSUMB\\CST205\\Module 3\\Lab 7\\ThanksgivingCard.jpg")

makeCard()
