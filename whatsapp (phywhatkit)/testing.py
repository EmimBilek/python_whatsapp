import pywhatkit
import time

#kirim pesan langsung, harus login whatsapp dulu ->
numandmsg = [
    {'nomor' : '+6281282805886', 'pesan' : 'test yup'},
    {'nomor' : '+628997670186', 'pesan' : 'test jang'},
]
for val in numandmsg:
    
    print(f'mengirim pesan ke {val.get('nomor')} ...')
    pywhatkit.sendwhatmsg_instantly(val.get('nomor'), val.get('pesan'), 20, True, 3)
    time.sleep(3) #jeda 

#kirim pesan sesuai waktu yang ditentukan ->
#pywhatkit.sendwhatmsg('+6281282805886', 'test yup', 13, 15)
#pywhatkit.sendwhatmsg('+628997670186', 'test jang', 13, 15)