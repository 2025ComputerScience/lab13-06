import pytesseract
from PIL import Image
import cv2

# 開啟圖片
image = Image.open("/content/Screenshot_20251226_204630_Samsung capture.jpg")

text = pytesseract.image_to_string(image, lang='chi_tra', config='--psm 11')

print("OCR 辨識結果:")
print("-" * 40)
print(text)