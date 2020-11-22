# Automatic Corona Report

import time
import re
import analize
import os
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pathlib import Path

ID = "324272202"  # Put your ID number here

path = Path(__file__).resolve().parent

mobile_emulation = {"deviceName": "Nexus 5"}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(os.path.join(path, r"chromedriver.exe"), options=chrome_options)
driver.get("https://clearance.medical.idf.il/")

id_in = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div[4]/div[1]/div/div/input")
id_in.send_keys(ID)
id_in.send_keys(Keys.ENTER)
time.sleep(5)

try:
    button = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/button")
    if button:
        button.click()
except NoSuchElementException:
    print("Its a new day!")

buttons = [
    driver.find_element(
        By.XPATH, "/html/body/div/div/div/div/div/div[2]/div[1]/div[2]/label[2]/span[1]/span[1]/input"),
    driver.find_element(
        By.XPATH, "/html/body/div/div/div/div/div/div[2]/div[2]/div[2]/label[2]/span[1]/span[1]/input")
]
for button in buttons:
    button.click()

image_path = os.path.join(path, "numbers.png")
driver.save_screenshot(image_path)
text = analize.run(image_path)

digits = re.findall(r"\d\d\d\d", text)
selected = digits[-1]
if len(selected) == 5:
    selected = selected[1::]

for i in range(4):
    num = driver.find_element(By.XPATH, f"/html/body/div/div/div/div/div/div[4]/div/input[{i+1}]")
    num.send_keys(selected[i])

driver.close()
os.system(fr"date /T >> {path}\autoCorona.log")

"""
import pywhatkit
import datetime
now = datetime.datetime.now().strftime("%H:%M").split(":")
text = "מילאתי שאלון קורונה"
pywhatkit.sendwhatmsg("+972506703016", text , int(now[0]), int(now[1]) + 3)
"""
