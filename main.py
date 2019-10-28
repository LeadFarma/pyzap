import webbrowser
import pyautogui as pygui , time

#whatsapp web
webbrowser.open('https://web.whatsapp.com')
#waiting load of whatsapp page
time.sleep(20)

contact = 'LeadFarma'
message = "Hello , I'm a robot"
#mouse point position
pygui.moveTo(x=525, y=317 , duration=0.7)
pygui.click()

pygui.typewrite(contact, interval = 0.04)
pygui.press('enter')
time.sleep(1)

pygui.typewrite(message, interval = 0.03)
pygui.press('enter')
print("Proccess completed")