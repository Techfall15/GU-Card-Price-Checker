from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service as ChromeService
import time
import re

# Main GODS Unchained URL: https://toke`ntrove.com/collection/GodsUnchainedCards

chrome_options = Options()
chrome_options.headless = False

driver = webdriver.Chrome(service=ChromeService(
    executable_path=ChromeDriverManager().install()),options=chrome_options)
driver.implicitly_wait(20)

driver.get("https://tokentrove.com/collection/GodsUnchainedCards")

search_bar = driver.find_element(by=By.CSS_SELECTOR, value="input[type='text']")
cardToSearch = "Humble Benefactor"
#cardToSearch = input("Enter Card Name: ")
search_bar.send_keys(cardToSearch)

w = WebDriverWait(driver, 10.0)

listing_information = w.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "listing-info")))

print("\nCard Name: {0}\n".format(cardToSearch))
count = 0
card_URLS = []
card_strings = [
    "{0:<15} {1:>12}".format("Meteorite", "$-.--"),
    "{0:<15} {1:>12}".format("Shadow", "$-.--"),
    "{0:<15} {1:>12}".format("Gold", "$-.--"),
    "{0:<15} {1:>12}".format("Diamond", "$-.--"),
]
for item in listing_information:
    item.click()
    card_URLS.append(driver.current_url)
    w = WebDriverWait(driver, 10.0)
    meta_data = w.until(EC.presence_of_element_located((By.CLASS_NAME, "order-details-metadata")))
    meta_data_rows = meta_data.find_elements(By.CLASS_NAME, "order-details-row")
    card_quality = meta_data_rows[2].find_element(By.CLASS_NAME, "order-details-value")
    price_table = w.until(EC.presence_of_element_located((By.CLASS_NAME, "ReactTable")))
    price_row = w.until(EC.presence_of_element_located((By.CLASS_NAME, "secondary-price-col")))
    match card_quality.text:
        case "Meteorite":
            card_strings[0] = "{0:<15} {1:>12}".format(card_quality.text, price_row.text)
        case "Shadow":
            card_strings[1] = "{0:<15} {1:>12}".format(card_quality.text, price_row.text)
        case "Gold":
            card_strings[2] = "{0:<15} {1:>12}".format(card_quality.text, price_row.text)
        case "Diamond":
            card_strings[3] = "{0:<15} {1:>12}".format(card_quality.text, price_row.text)
        case _:
            print("Error Finding Card Data")
    
    driver.back()
    time.sleep(0.6)

for string in card_strings:
    print(string)
    
    


#for item in listing_information:
#    listing_price = item.find_element(by=By.CLASS_NAME, value="listing-price-container")
#    eth_price = item.find_element(by=By.CLASS_NAME, value="listing-price-primary")
#    dollar_price = item.find_element(by=By.CLASS_NAME, value="listing-price-secondary")
#    match count:
#        case 0:
#            print("M Price: " + dollar_price.text)
#        case 1:
#            print("S Price: " + dollar_price.text)
#        case 2:
#            print("G Price: " + dollar_price.text)
#        case 3:
#            print("D Price: " + dollar_price.text)
#        case _:
#            print("There was a problem fetching card prices")
#    count += 1

print("\nEnd of Data")