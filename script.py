import os
from PIL import Image
from pytesseract import *


save_path = os.getcwd()+"\\output_text"
input_path = os.getcwd()+"\\input_image"
tesseract_path = os.getcwd()+"\\Tesseract-OCR\\tesseract.exe"
tesseract_tessdata_path = os.getcwd()+"\\Tesseract-OCR\\tessdata"
os.chdir(input_path)
image_name=os.listdir()
image_name=image_name[0]
image_name_split=os.path.splitext(image_name)
img_path = os.getcwd()+"\\"+image_name
img=Image.open(img_path)
pytesseract.tesseract_cmd = tesseract_path
tessdata_dir_config = r'--tessdata-dir "'+tesseract_tessdata_path+'"'
txt= image_to_string(img,lang='eng+fra',config=tessdata_dir_config)
file1 = open(os.path.join(save_path, "output_text.txt"), "w")
file1.write(txt)
file1.close()
print(txt)