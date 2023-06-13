from PIL import Image
import math

def toNegative(image):
  w = image.size[0]
  h = image.size[1]
  for y in range(0, h): #each pixel has coordinates
    for x in range(0, w):
      R, G, B = im.getpixel((x, y))
      nR = 255- R
      nG = 255- G
      nB = 255- B
      image.putpixel((x,y) , (nR, nG, nB))
  image.show()

def toGray(image):
  w = image.size[0]
  h = image.size[1]
  for y in range(0, h): #each pixel has coordinates
    for x in range(0, w):
      R, G, B = im.getpixel((x, y))
      image.putpixel((x,y) , (R, G, B))
  image.show()


im = Image.open('gato2.jpg') #your image

toGray(im)