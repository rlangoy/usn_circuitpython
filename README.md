# usn_circuitpython
Circuit Python tool library used at USN

Class CPImageWriter is used to display monocrome .bmp .pgm and .pbm
(Windows Bitmap, Portable GrayMap and Portable BitMap) on a OLED display

example:
```python
import adafruit_ssd1306
import busio
from board import *
import adafruit_framebuf
from usn_circuitpython import CPImageWriter

i2c = busio.I2C(P0_20, P0_22)
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
image =CPImageWriter(disp)
image.write_pbm_img(name='img/heart-16x16.pbm',invert=True)
image.write_pbm_img(name='img/temperature-16x16.pbm',offX=16,invert=True)
image.write_pbm_img(name='img/temperature-32x32.pbm',offY=16,invert=True)
image.write_bmp_img(name="img/checkbox-checked-32x32.bmp",offX=32,offY=16,invert=True)
image.write_bmp_img(name="img/checkbox-unchecked-32x32.bmp",offX=64,offY=16,invert=True)
disp.show()
```

