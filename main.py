from PIL import Image
import math
im = Image.open('./malp_whatsapp.jpg') #your image

def toNegative(image):
  w = image.size[0]
  h = image.size[1]
  for y in range(0, h): #each pixel has coordinates
    for x in range(0, w):
      R, G, B = image.getpixel((x, y))
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
      R, G, B = image.getpixel((x, y))
      media = round((R * 0.2126) + (G * 0.7152) + (B * 0.0722))
      image.putpixel((x,y) , (media, media, media))
  image.show()

def toSepia(image):
  w = image.size[0]
  h = image.size[1]
  for y in range(0, h):
    for x in range(0, w):
      R, G, B = image.getpixel((x, y))
      nR = round(R * 0.393 + G * 0.769 + B * 0.189)
      nG = round(R * 0.349 + G * 0.686 + B * 0.168)
      nB = round(R * 0.272 + G * 0.534 + B * 0.131)
      image.putpixel((x,y), (nR, nG, nB))
  image.show()

def toBW(image):
  w = image.size[0]
  h = image.size[1]
  for y in range(0, h):
    for x in range(0, w):
      R, G, B = image.getpixel((x, y))

      soma = round(R + G + B)

      if (soma > 190):
        nR = 255
        nG = 255
        nB = 255
      else:
        nR = 0
        nG = 0
        nB = 0

      image.putpixel((x,y), (nR, nG, nB))
  image.show()

def changeChannels(image):
  w = image.size[0]
  h = image.size[1]
  for y in range(0, h):
    for x in range(0, w):
      R, G, B = image.getpixel((x, y))

      image.putpixel((x, y), (G, B, R))
  image.show()

def increaseRed(image):
  w = image.size[0]
  h = image.size[1]
  for y in range(0, h):
    for x in range(0, w):
      R, G, B = image.getpixel((x, y))

      nR = round(R * 1.1)

      image.putpixel((x, y), (nR, G, B))
  image.show()

def increaseGreen(image):
  w = image.size[0]
  h = image.size[1]
  for y in range(0, h):
    for x in range(0, w):
      R, G, B = image.getpixel((x, y))

      nG = round(G * 1.1)

      image.putpixel((x, y), (R, nG, B))
  image.show()

def increaseBlue(image):
  w = image.size[0]
  h = image.size[1]
  for y in range(0, h):
    for x in range(0, w):
      R, G, B = image.getpixel((x, y))

      nB = round(B * 1.1)

      image.putpixel((x, y), (R, G, nB))
  image.show()


def increaseBrightness(image):
  w = image.size[0]
  h = image.size[1]
  for y in range(0, h):
    for x in range(0, w):
      R, G, B = image.getpixel((x, y))

      nR = round(R * 1.2)
      nG = round(G * 1.2)
      nB = round(B * 1.2)

      image.putpixel((x, y), (nR, nG, nB))
  image.show()

def decreaseBrightness(image):
  w = image.size[0]
  h = image.size[1]
  for y in range(0, h):
    for x in range(0, w):
      R, G, B = image.getpixel((x, y))

      nR = round(R * 0.8)
      nG = round(G * 0.8)
      nB = round(B * 0.8)

      image.putpixel((x, y), (nR, nG, nB))
  image.show()

def toBlur(image):
  w = image.size[0]
  h = image.size[1]
  for y in range(1, h-1):
    for x in range(1, w-1):
      ra, ga, ba = image.getpixel((x-1, y-1))
      rb, gb, bb = image.getpixel((x, y-1))
      rc, gc, bc = image.getpixel((x+1, y-1))

      ra1, ga1, ba1 = image.getpixel((x-1, y))
      rb1, gb1, bb1 = image.getpixel((x, y))
      rc1, gc1, bc1 = image.getpixel((x+1, y))

      ra2, ga2, ba2 = image.getpixel((x-1, y+1))
      rb2, gb2, bb2 = image.getpixel((x, y+1))
      rc2, gc2, bc2 = image.getpixel((x+1, y+1))

      nR = round((ra + rb + rc + ra1 + rb1 + rc1 + ra2 + rb2 + rc2) / 9)
      nG = round((ga + gb + gc + ga1 + gb1 + gc1 + ga2 + gb2 + gc2) / 9)
      nB = round((ba + bb + bc + ba1 + bb1 + bc1 + ba2 + bb2 + bc2) / 9)

      image.putpixel((x, y), (nR, nG, nB))
  image.show()

# toGray(im)
# toNegative(im)
# toSepia(im)
# toBW(im)
changeChannels(im)
# increaseRed(im)
# increaseGreen(im)
# increaseBlue(im)
# increaseBrightness(im)
# decreaseBrightness(im)
# toBlur(im)