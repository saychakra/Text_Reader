import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open("writing_test.png") # the second one 
# im = im.filter(ImageFilter.MedianFilter())
# enhancer = ImageEnhance.Contrast(im)
# im = enhancer.enhance(2)
# im = im.convert('1')
# im.save('temp.png')
text = pytesseract.image_to_string(Image.open('writing_test.png'))
print(text)