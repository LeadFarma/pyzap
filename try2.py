
import os
import pyautogui as pygui , time
import Xlib.display
from time import sleep
from selenium import webdriver
from pyvirtualdisplay.smartdisplay import SmartDisplay


display = SmartDisplay(visible=0, size=(1920, 1080))
display.start()
browser = webdriver.Firefox()
browser.get('https://web.whatsapp.com')
sleep(20)
print('entrando no display')

pygui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])
#try:
contact = 'LeadFarma'
message = "Hello , I'm a robot"
#mouse point position

pygui.screenshot()
pygui.moveTo(x=525, y=317 , duration=0.7)
pygui.click()

pygui.typewrite(contact, interval = 0.04)
pygui.press('enter')
time.sleep(1)

pygui.typewrite(message, interval = 0.03)
pygui.press('enter')
print("Proccess completed")

    
#except:
 #   print "deu ruim"

browser.quit()
display.stop()