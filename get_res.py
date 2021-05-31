import os
import os.path
import zipfile

import requests

qs_font_url = "https://fonts.google.com/download?family=Quattrocento%20Sans"
lsb_font_url = "https://communication.cph.org/hubfs/_music/lutheran-service-builder/LSBSymbol.ttf"

print("Creating res/fonts directory")
os.makedirs("res/fonts", exist_ok=True)

start = os.getcwd()
os.chdir("res/fonts")
print("Downloading Quattrocento Sans font...")
qs = requests.get(qs_font_url, allow_redirects=True)
with open("quattrocento_sans.zip", "wb") as zf:
    zf.write(qs.content)
with zipfile.ZipFile("quattrocento_sans.zip", "r") as zf:
    zf.extractall(".")
os.unlink("quattrocento_sans.zip")

print("Downloading LSBSymbol.ttf...")
lsb = requests.get(lsb_font_url, allow_redirects=True)
with open("LSBSymbol.ttf", "wb") as lsb_ttf:
    lsb_ttf.write(lsb.content)

os.chdir(start)