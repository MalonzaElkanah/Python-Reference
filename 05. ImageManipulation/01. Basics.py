from PIL import ImageColor, Image, ImageDraw, ImageFont
import os

# Get Color Codes
red = ImageColor.getcolor('red', 'RGB')
green = ImageColor.getcolor('green', 'RGBA')
print(red, ' ', green)

# open Image and get Its properties
myPic = Image.open('./images/pic1.jpg')
print("Width, height: ", myPic.size, "\nFormat: ",
      myPic.format, "\nFilename: ", myPic.filename, "\nFormat Description: ", myPic.format_description)

# create a new Image
im = Image.new('RGBA', (100, 200), 'purple')
im.save('./images/purpleImage.png')
im2 = Image.new('RGBA', (20, 20))
im2.save('./images/transparentImage.png')

# Cropping Images
im = Image.open('./images/purpleImage.png')
croppedIm = im.crop((5, 5, 50, 50))
croppedIm.save('./images/cropImage.png')

# Paste Image
print(croppedIm.size)
myPic.paste(croppedIm, (0, 0))
myPic.save('./images/pasted.png')

# Resize Image
width, height = im.size
quartersizedIm = im.resize((int(width / 2), int(height / 2)))
quartersizedIm.save('./images/quartersized.png')
svelteIm = im.resize((width, height + 300))
svelteIm.save('./images/svelte.png')

# Rotating and Flipping Images
myPic.rotate(90).save('./images/rotated90.png')
myPic.rotate(180).save('./images/rotated180.png')
myPic.rotate(270, expand=True).save('./images/rotated270.png')

myPic.rotate(6).save('./images/rotated6.png')
myPic.rotate(6, expand=True).save('./images/rotated6_expanded.png')

# mirror flip
myPic.transpose(Image.FLIP_LEFT_RIGHT).save('./images/horizontal_flip.png')
myPic.transpose(Image.FLIP_TOP_BOTTOM).save('./images/vertical_flip.png')

# Changing Individual Pixels
# getpixel()      -     retrieve the color of a pixel
# putpixel()      -     set the color of a pixel
colour = im.getpixel((0, 0))
print(colour)
newPic = Image.open('./images/pic2.jpg')
for x in range(100):
    for y in range(50, 100):
        newPic.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
newPic.getpixel((0, 0))
newPic.getpixel((0, 50))
newPic.save('./images/putPixel.png')

# Drawing on Image File
drw_im = Image.new('RGBA', (200, 200), 'white')  # create a new image a 200×200 white image
draw1 = ImageDraw.Draw(drw_im)   # pass the Image object to the ImageDraw.Draw() function to receive an ImageDraw object

# This object has several methods for drawing shapes and text onto an Image object.

# point(xy, fill)   -   method draws individual pixels.
# line(xy, fill, width) -  method draws a line or series of lines

# xy argument represents a list of the points you want to draw. The list can be a list of x- and y-coordinate tuples,
# The fill argument is the color of the points and is either an RGBA tuple or a string ofa color name, such as 'red'.
# width argument is the width of the lines and defaults to 1 if left unspecified.


# rectangle(xy, fill, outline) method draws a rectangle.
# The xy argument is a box tuple of the form (left, top, right, bottom) .
# The left and top values specify the x- and y-coordinates of the upper-left corner of the rect- while right and
# bottom specify the lower-right corner

# ellipse(xy, fill, outline) method draws an ellipse.
# If the width and height of the ellipse are identical, this method will draw a circle. The xy
# argument is a box tuple ( left , top , right , bottom ) that represents a box that precisely contains the ellipse.

# The polygon(xy, fill, outline) method draws an arbitrary polygon.
# The xy argument is a list of tuples, such as [(x, y), (x, y), ...] , or integers, such
# as [x1, y1, x2, y2, ...] , representing the connecting points of the polygon’s sides.
# The last pair of coordinates will be automatically connected to the first pair.

im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)
draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
draw.rectangle((20, 30, 60, 60), fill='blue')
draw.ellipse((120, 30, 160, 60), fill='red')
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')
for i in range(100, 200, 10):
    draw.line([(i, 0), (200, i - 100)], fill='green')
im.save('./images/drawing.png')

# Drawing Text

# text() method takes four arguments: xy , text , fill , and font .
# xy argument is a two-integer tuple specifying the upper-left corner of the text box.
# The text argument is the string of text you want to write. The optional fill argument is the color of the text.
# The optional font argument is an ImageFont object, used to set the type- face and size of the text.

draw.text((20, 150), 'Hello', fill='purple')
# fontsFolder = '/usr/share/fonts/truetype'  # e.g. ‘/Library/Fonts’
# arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
# draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
im.save('./images/text.png')
