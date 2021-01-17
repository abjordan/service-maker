#!/usr/bin/env python

from PIL import Image, ImageFont, ImageDraw
import json

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

with open('config.json', 'r') as conffile:
    config = json.load(conffile)

sym_font = ImageFont.truetype(config['fonts']['symbol'])
heading_font = ImageFont.truetype(config['fonts']['bold-italic'], size=40)


bottom_third_size = (1920, 214)

img = Image.new('RGBA', bottom_third_size, color='white')

logo_fs = Image.open(config['logo_file'])

logo = logo_fs.resize((174, 174), Image.LANCZOS)

# Third parameter here is an Image to use as a mask. Assuming
# the logo is saved with an alpha channel, this will respect
# the transparency that may or may not be present.
#img.paste(logo, (20, 20, 194, 194), logo)
img.paste(logo, (20, 20), logo)

d = ImageDraw.Draw(img)

d.text( (1014, 14), "Test", font=heading_font, fill='black')

img.save('test.png')

