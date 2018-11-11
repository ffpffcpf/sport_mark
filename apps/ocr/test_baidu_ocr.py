from aip import AipOcr
from sport_mark.settings import BASE_DIR

""" 你的 APPID AK SK """
APP_ID = '14757744'
API_KEY = 'q6mdaiiO2xg7omS0irC6jOlx'
SECRET_KEY = 'FG1hxeWTNiRxgNqih8cHAdGhDvhi3yHg'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content(BASE_DIR+'/media/test4.jpg')
s = client.handwriting(image)
print(s)