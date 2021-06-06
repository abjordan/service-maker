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

sym_font = ImageFont.truetype(config['fonts']['symbol'], size=52)
heading_font = ImageFont.truetype(config['fonts']['bold-italic'], size=68)
text_font = ImageFont.truetype(config['fonts']['regular'], size=52)
bold_font = ImageFont.truetype(config['fonts']['bold'], size=52)

bottom_third_size = (3230, 360)

img = Image.new('RGBA', bottom_third_size, color='white')

logo_fs = Image.open(config['logo_file'])

logo = logo_fs.resize((280, 280), Image.LANCZOS)

# Third parameter here is an Image to use as a mask. Assuming
# the logo is saved with an alpha channel, this will respect
# the transparency that may or may not be present.
#img.paste(logo, (20, 20, 194, 194), logo)
img.paste(logo, (60, 40), logo)

d = ImageDraw.Draw(img)

d.text( (1014, 14), "Test", font=heading_font, fill='black')

d.text( (550, 100), "P", font=sym_font, fill='black')
d.text( (675, 105), "This is the day the Lord has made!", font=text_font, fill='black')

img.save('test.png')

