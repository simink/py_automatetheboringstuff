### Chapter 19 - Manipulating Images

# computer image fundamentals -------------------------------------------------

from PIL import ImageColor
ImageColor.getcolor('red', 'RGBA')
ImageColor.getcolor('cornflowerblue', 'RGBA')

# manipulating images --------------
from PIL import Image
catIm = Image.open('../data/zophie.png')
catIm.size
width, height = catIm.size
width
height
catIm.filename
catIm.format
catIm.format_description
catIm.save('../data/zophie.jpg')

# new image -----
from PIL import Image
im = Image.new('RGBA', (100, 200), 'purple')
im.save('../data/purpleImage.png')
im2 = Image.new('RGBA', (20, 20))
im2.save('../data/transparentImage.png')

# cropped image -------------
catIm = Image.open('../data/zophie.png')
croppedIm = catIm.crop((335, 345, 565, 560))
croppedIm.save('../data/cropped.png')

# copy paste onto other images
catIm = Image.open('../data/zophie.png')
catCopyIm = catIm.copy()
faceIm = catIm.crop((335, 345, 565, 560))
faceIm.size
catCopyIm.paste(faceIm, (0, 0))
catCopyIm.paste(faceIm, (400, 500))
catCopyIm.save('../data/pasted.png')

# tile image across entire image -----
catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catIm.copy()
for left in range(0, catImWidth, faceImWidth):
    for top in range(0, catImHeight, faceImHeight):
        print(left, top)
        catCopyTwo.paste(faceIm, (left, top))

catCopyTwo.save('../data/tiled.png')

## resize image -----
catIm = Image.open('../data/zophie.png')
width, height = catIm.size
quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
quartersizedIm.save('../data/quartersized.png')
svelteIm = catIm.resize((width, height + 300))
svelteIm.save('../data/svelte.png')

## rotating image -----
catIm = Image.open('../data/zophie.png')
catIm.rotate(90).save('../data/rotated90.png')
catIm.rotate(180).save('../data/rotated180.png')
catIm.rotate(270).save('../data/rotated270.png')
catIm.rotate(6).save('../data/rotated6.png')
catIm.rotate(6, expand=True).save('../data/rotated6_expanded.png')

# mirror flip
catIm.transpose(Image.FLIP_LEFT_RIGHT).save('../data/horizontal_flip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('../data/vertical_flip.png')

# change individual pixel ------------
im = Image.new('RGBA', (100, 100))
im.getpixel((0, 0))
for x in range(100):
    for y in range(50):
        im.putpixel((x, y), (210, 210, 210))

from PIL import ImageColor
for x in range(100):
    for y in range(50, 100):
        im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))

im.getpixel((0, 0))
im.getpixel((0, 50))
im.save('../data/putPixel.png')


# drawing shapes ----------------
from PIL import Image, ImageDraw
im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)
draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
draw.rectangle((20, 30, 60, 60), fill='blue')
draw.ellipse((120, 30, 160, 60), fill='red')
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')
for i in range(100, 200, 10):
    draw.line([(i, 0), (200, i - 100)], fill='green')

im.save('../data/drawing.png')


## drawing text ------------
from PIL import Image, ImageDraw, ImageFont
import os
im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)
draw.text((20, 150), 'Hello', fill='purple')
fontsFolder = 'FONT_FOLDER' # e.g. ‘/Library/Fonts'
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
im.save('../data/text.png')