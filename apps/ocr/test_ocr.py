from PIL import Image
import pytesseract
from sport_mark.settings import BASE_DIR
words = pytesseract.image_to_string(Image.open(BASE_DIR+'/media/test4.jpg'), lang='chi_sim')
print(words)


