# package yang dibutuhkan untuk whatsapp selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

#coding
driver = webdriver.Chrome() #variabel browser chrome

baseurl = "https://web.whatsapp.com" #url whatsapp

driver.get(baseurl) #membuka browser chrome dengan url whatsapp

input("Tekan enter setelah scan qr") #tekan enter setelah scan qr

with open("contacts.csv", newline="") as csvfile: #buka file contacts.csv
    
    readContact = csv.reader(csvfile)

    for phone,message in readContact:

        phonenum = phone
        msg = message

        print(f"mengirim pesan ke {phonenum}")

        sametab = (baseurl + "/send?phone=" + str(phonenum)) #url untuk mengirim ke nomor tertentu

        driver.get(sametab) #buka chrome pake url sametab

        time.sleep(45) #jeda, sesuaikan dengan kecepatan internet

        content = driver.switch_to.active_element

        content.send_keys(msg) #menuliskan pesan di text pesan

        content.send_keys(Keys.RETURN) #menekan tombol enter setelah menuliskan pesan

        time.sleep(3) # jeda untuk mengirimkan pesan yang lain, sesuaikan dengan kecepatan internet kamu