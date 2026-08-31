from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


options = Options() 
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)
options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])

driver.get("https://www.google.com")

a = driver.find_element(by=By.CLASS_NAME, value="gLFyf")
a.send_keys("f")
time.sleep(2)
a.send_keys("a")
time.sleep(2)
a.send_keys("c")
time.sleep(2)
a.send_keys("e")
time.sleep(2)
a.send_keys("b")
time.sleep(2)
a.send_keys("o")
time.sleep(2)
a.send_keys("o")
time.sleep(3)
a.send_keys("k")
time.sleep(2)

a.send_keys(Keys.ENTER)
time.sleep(5)
first_link= driver.find_element(by=By.CLASS_NAME, value="zReHs").click()
#first_link.click#
Email_id = driver.find_element(by=By.CLASS_NAME ,value ="x10d0gm4 x1fhayk4 x3cjxhe x1al4vs7 x12scifz xmper1u xdg88n9 xzwoauc x193iq5w x6ikm8r x10wlt62 x47corl x10l6tqk xlyipyv x1d7kzl9 xii2z7h x11xpdln x1r7x56h xuxw1ft xp5op4 x1y44fgy xdzva22 xs8nzd4 x1fzehxr xha3pab")
time.sleep(2)
Email_id.send_keys("7398105303")
Password = driver.find_element(by=By.CLASS_NAME, value= "x10d0gm4 x1fhayk4 x3cjxhe x1al4vs7 x12scifz xmper1u xdg88n9 xzwoauc x193iq5w x6ikm8r x10wlt62 x47corl x10l6tqk xlyipyv x1d7kzl9 xii2z7h x11xpdln x1r7x56h xuxw1ft xp5op4 x1y44fgy xdzva22 xs8nzd4 x1fzehxr xha3pab")
Password.send_keys("Pran@9956")

input("Press Enter to close...")

driver.quit()