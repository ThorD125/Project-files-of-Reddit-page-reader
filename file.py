# initializing
from get_gecko_driver import GetGeckoDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from gtts import gTTS
from playsound import playsound
import os
import time
get_driver = GetGeckoDriver()
get_driver.install()



# open browser
driver = webdriver.Firefox()

# request page url

# inputredditlink = "https://www.reddit.com/r/showertoughts/"
inputredditlink = input("Please input the reddit page link")
driver.get(inputredditlink)


# get titel
title = driver.find_element_by_tag_name("h1").text
print(title)
audiotitle = 'title' + '.mp3'
language = 'en'
afspeletitle = gTTS(text = title, lang = language, slow = False)
afspeletitle.save(audiotitle)
playsound(audiotitle)
os.remove(audiotitle)

# click items
driver.execute_script("""
document.querySelectorAll('._1tI68pPnLBjR1iHcL7vsee')[0].click();
document.getElementsByClassName('M2Hk_S2yvXpsNPfZMBMur ')[1].click()
""")


# delete extra items
driver.execute_script("""
document.querySelectorAll('.q4a8asWOWdfdniAbgNhMh')[0].remove();
""")
driver.execute_script("""
document.querySelectorAll('._1BFbVxT49QnrAN3fqGZ1z8')[0].remove();
""")
driver.execute_script("""
document.querySelectorAll('header')[0].remove();
""")
driver.execute_script("""
document.querySelectorAll('.wBtTDilkW_rtT2k5x3eie')[0].remove();
""")




driver.execute_script("""
x=document.querySelectorAll('._23h0-EcaBUorIHC-JZyh6J').length
for (x; x>0; x--){
document.querySelectorAll('._23h0-EcaBUorIHC-JZyh6J')[0].remove();}
""")
driver.execute_script("""
x=document.querySelectorAll('._14-YvdFiW5iVvfe5wdgmET').length
for (x; x>0; x--){
document.querySelectorAll('._14-YvdFiW5iVvfe5wdgmET')[0].remove();}
""")
driver.execute_script("""
x=document.querySelectorAll('._1ixsU4oQRnNfZ91jhBU74y').length
for (x; x>0; x--){
document.querySelectorAll('._1ixsU4oQRnNfZ91jhBU74y')[0].remove();}
""")
driver.execute_script("""
x=document.querySelectorAll('._3-miAEojrCvx_4FQ8x3P-s').length
for (x; x>0; x--){
document.querySelectorAll('._3-miAEojrCvx_4FQ8x3P-s')[0].remove();}
""")

time.sleep(5)

# loop
inputnumbe = input("Please enter how many post's you want to hear")
# for i in range(10):
for i in range(int(inputnumbe)):
    # TODO numbering
    print(i)
    driver.execute_script("""
    x=document.querySelectorAll('._23h0-EcaBUorIHC-JZyh6J').length
    for (x; x>0; x--){
    document.querySelectorAll('._23h0-EcaBUorIHC-JZyh6J')[0].remove();}
    """)
    driver.execute_script("""
    x=document.querySelectorAll('._14-YvdFiW5iVvfe5wdgmET').length
    for (x; x>0; x--){
    document.querySelectorAll('._14-YvdFiW5iVvfe5wdgmET')[0].remove();}
    """)
    driver.execute_script("""
    x=document.querySelectorAll('._1ixsU4oQRnNfZ91jhBU74y').length
    for (x; x>0; x--){
    document.querySelectorAll('._1ixsU4oQRnNfZ91jhBU74y')[0].remove();}
    """)
    driver.execute_script("""
    x=document.querySelectorAll('._3-miAEojrCvx_4FQ8x3P-s').length
    for (x; x>0; x--){
    document.querySelectorAll('._3-miAEojrCvx_4FQ8x3P-s')[0].remove();}
    """)
    # remove previous read item
    driver.execute_script("""
    window.scrollTo(0, 500);
    """)
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".rpBJOHq2PR60pnwJlUyP0")))
    finally:
        driver.execute_script("""
        document.querySelectorAll('.rpBJOHq2PR60pnwJlUyP0')[0].firstChild.remove()
        """)
        # wait until item found proceed 
        try:
            elemenet = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "._1oQyIsiPHYt6nx7VOmd1sz")))
        finally:
            # delete found item 
            texter = driver.find_element_by_class_name("_1oQyIsiPHYt6nx7VOmd1sz").text
            print(texter)
            audiotext = 'reddit' + str(i) + '.mp3'
            afspele = gTTS(text = texter, lang = 'en', slow = False)
            afspele.save(audiotext)
            playsound(audiotext)
            os.remove(audiotext)
driver.quit()