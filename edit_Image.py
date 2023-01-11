# from PIL import Image
# import os
# img1=Image.open('Dog1.jpg')

# for converting the extension
# img1.save('Dog1.png')

#for viewing the image
# img1.show()

#resize image
# max_size=(250,250)
# img1.thumbnail(max_size)
# img1.save('Dog1small.jpg')


# creating multiple files
# for item in os.listdir():
#     if item.endswith('.jpg'):
#         img1=Image.open(item)
#         filename,extension=os.path.splitext(item)
#         img1.save(f'{filename}.png')

from PIL import Image ,ImageEnhance
import os

img1=Image.open('Dog1.jpg')

# enhancer=ImageEnhance.Sharpness(img1)
# enhancer.enhance(2).save('dog1edited.jpg')

enhancer=ImageEnhance.Color(img1)
enhancer.enhance(0).save('dog1edited.jpg')

# enhancer=ImageEnhance.Sharpness(img1)
# enhancer.enhance(2).save('dog1edited.jpg')