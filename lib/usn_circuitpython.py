"""
``
====================================================
Image viewer for the  Adafruit SSD1306 OLED driver
* Author :Rune Langøy
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/rlangoy/usn_circuitpython.git"

import adafruit_ssd1306

class CPImageWriter:
    def __init__(self, disp ):
        self.disp = disp
   
    # Portable BitMap ASCII_magic: P4 .pbm 0–1 (white & black)
    def write_pbm_img(self,name='aa.pbm', offX=0,offY=0,invert=False):
        f=open(name, 'rb')
        magic=f.readline() # Magic number (P1 - BitMap , P2 - GrayMap, P3 - PixMap)
        if magic==b'P4\n' :
            f.readline() # Read Creator info
        xDim ,yDim =list(map(int,f.readline().decode().split())) # read dimensions as integers
        data = bytearray(f.read())
        for x in range(xDim//8):   # x range in bytes while data is in bits
            for y in range(yDim):
                byteData = data[x + y*xDim//8]
                for n in range(8):                            
                  if invert :
                     c = ((byteData<<n) & (0x80))
                  else :
                      c = not ((byteData<<n) & (0x80))
                      
                  self.disp.pixel(offX+x*8+n,offY+y, c )

    # Portable GrayMap ASCII_MAGIC P5 .pgm 0–255 (gray scale)
    def write_pgm_img(self,name='aa.pgm',offX=0,offY=0,invert=False):
        f=open(name, 'rb')
        magic=f.readline() # Magic number (P1 - BitMap , P2 - GrayMap, P3 - PixMap)
        if magic==b'P5\n' :
            f.readline()   # Read Creator info

        xDim ,yDim =list(map(int,f.readline().decode().split())) # read dimensions as integers
        f.readline()       # Max grey Level
        data = bytearray(f.read())

        for x in range(xDim):
            for y in range(yDim):
                c = data[x + y*xDim]
                if invert :
                    self.disp.pixel(x+offX, y+offY, c<128 )
                else:
                    self.disp.pixel(x+offX, y+offY, c>128 )
