from PIL import Image
import pytesseract
import pyautogui
import time

accept = '\accept.jpg'
pytesseract.pytesseract.tesseract_cmd = \
    r'C:\Users\iunth\AppData\Local\Programs\Tesseract-OCR\tesseract'

acceptImage = pyautogui.screenshot(region=(599,587,733,198))
acceptWord = pytesseract.image_to_string(acceptImage)
#findmatch = pyautogui.locateOnScreen('findMatch.png',confidence=0.5)
#pyautogui.click(findmatch)
#Bigger photo for locating queue pop        Box(left=599, top=587, width=733, height=198)
while acceptWord != 'ACCEPT!':
    acceptImage = pyautogui.screenshot(region=(599,587,733,198))
    acceptWord = pytesseract.image_to_string(acceptImage)
    print("Waiting for queue pop...")
    #print(acceptWord)
    if 'ACCEPT!' in acceptWord:
        accept = pyautogui.locateOnScreen(accept,confidence=0.8)
        print(acceptWord)
        pyautogui.moveTo(accept)
        pyautogui.click()
        break