from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = '/Users/admin/Downloads/chromedriver'
driver = webdriver.Chrome(PATH)

# Finds 6.5 Creedmoor Gold Ammo (Match) Federal Premium

driver.get('https://www.federalpremium.com/rifle/fusion/')

tracking_consent_button = driver.find_element_by_class_name('affirm')
tracking_consent_button.click()

rifle = driver.find_element_by_link_text('Rifle')
rifle.click()


creedmoor_div = driver.find_element_by_id('header-refinement-caliber')
creedmoor_div.click()


creedmoor_list = driver.find_element_by_xpath(".//label[@for='6.5 Creedmoor']")
creedmoor_list.click()

time.sleep(5)

products = driver.find_elements_by_class_name('col-lg-4')


for x in range(12):
    if products[x].find_element_by_class_name('label-1').text == 'Currently Unavailable':
        continue
    else:
        nme = products[x].find_element_by_class_name('pdp-link').text
        lnk = products[x].find_element_by_link_text(nme).get_attribute("href")
        prce = products[x].find_element_by_xpath(".//span[@class='value']").text
        res = "Ammo: " + nme + "\n" + "Price: " + prce + "\n" + "Link: " + lnk

        print(res)

