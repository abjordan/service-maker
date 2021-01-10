#!/usr/bin/env python

from PIL import Image, ImageFont, ImageDraw

# Need the logo

# Divide the region into blocks, based on how many lines of text
# we need.
# 
#   ==========================================================
#  |                         _Part of the Service_
#  |  LOGO      [P] This is the day the Lord has made;
#  |  LOGO      [C] Let us rejoice and be glad in in!
#  |  LOGO      
#   ==========================================================

bottom_third_size = (1920, 214)

img = Image.new('RGB', bottom_third_size, color='white')

img.save('test.png')

