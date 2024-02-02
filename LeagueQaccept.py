from PIL import Image
import pytesseract
import pyautogui

pytesseract.pytesseract.tesseract_cmd = \
    r'C:\Users\iunth\AppData\Local\Programs\Tesseract-OCR\tesseract'

acceptImage = pyautogui.screenshot(region=(599,587,733,198)) #Takes a picture of where would the queue pop appear (Only works when league is at full resolution and is in the middle of the screen).
acceptWord = pytesseract.image_to_string(acceptImage) #Converts the previous picture to text to locate where the ACCEPT! button would be.
print("Waiting for queue pop...")

while acceptWord != 'ACCEPT!':
    #while loop to keep looking constantly for the queue pop, by the method used in line 10,11
    acceptImage = pyautogui.screenshot(region=(599,587,733,198))
    acceptWord = pytesseract.image_to_string(acceptImage)
    
    if 'ACCEPT!' in acceptWord:
        #acceptWord Prints out a lot of random text, but the word ACCEPT! is somewhere there, so it looks for the substring ACCEPT! there.
        
        accept = pyautogui.locateOnScreen('accept.jpg',confidence=0.8)
        #Locates where the ACCEPT! button is, provided the picture of what it looks like for the program to find.
        
        pyautogui.moveTo(accept)
        pyautogui.click()
        break
