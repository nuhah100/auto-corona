# Automatic Corona Report

import time
import re
import analize
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ID = "324272202"  # Put your ID number here

mobile_emulation = {"deviceName": "Nexus 5"}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://clearance.medical.idf.il/")

id_in = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div[4]/div[1]/div/div/input")
id_in.send_keys(ID)
id_in.send_keys(Keys.ENTER)
time.sleep(5)

button = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/button")
if button:
    button.click()

buttons = [
    driver.find_element(
        By.XPATH, "/html/body/div/div/div/div/div/div[2]/div[1]/div[2]/label[2]/span[1]/span[1]/input"),
    driver.find_element(
        By.XPATH, "/html/body/div/div/div/div/div/div[2]/div[2]/div[2]/label[2]/span[1]/span[1]/input")
]
for button in buttons:
    button.click()

image_path = "numbers.png"
driver.save_screenshot(image_path)
text = analize.run(image_path)

digits = re.findall(r"\d\d\d\d", text)
selected = digits[-1]

for i in range(4):
    num = driver.find_element(By.XPATH, f"/html/body/div/div/div/div/div/div[4]/div/input[{i+1}]")
    num.send_keys(selected[i])

"""
import pywhatkit
import datetime
now = datetime.datetime.now().strftime("%H:%M").split(":")
pywhatkit.sendwhatmsg("+972506703016", "👍🏻" , int(now[0]), int(now[1]) + 3)
"""
