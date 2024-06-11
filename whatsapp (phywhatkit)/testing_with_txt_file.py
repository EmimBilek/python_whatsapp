import pywhatkit, pyautogui, time

#kirim pesan langsung
with open('msg.txt', 'r') as msgfile:
    msg = msgfile.read()

pywhatkit.sendwhatmsg_instantly('+6281282805886', msg, 15, True, 3)

# kirim pesan sesuai waktu yang ditentukan
# pywhatkit.sendwhatmsg('+628997670186', msg, 14, 8)
# pywhatkit.sendwhatmsg('+6281282805886', msg, 14, 9)
# time.sleep(1)
# pyautogui.click()
# time.sleep(1)
# pyautogui.press('enter')

#NB : kalo pake pywhatkit harus login whatsapp dulu