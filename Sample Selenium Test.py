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

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")

cardToSearch = input("Enter Card Name: ")
while (cardToSearch != "quit"):

    

    # Main GODS Unchained URL: https://toke`ntrove.com/collection/GodsUnchainedCards

    # Set up driver with edited chrome options
    driver = webdriver.Chrome(service=ChromeService(
        executable_path=ChromeDriverManager().install()),options=chrome_options)

    # Set wait time for java elements to appear
    driver.implicitly_wait(10)

    # URL to the totken trove for Gods Unchained (change for different collections)
    driver.get("https://tokentrove.com/collection/GodsUnchainedCards")

    # Find the search bar to search for cards
    search_bar = driver.find_element(by=By.CSS_SELECTOR, value="input[type='text']")

    # Push the card name the user wants into the search bar, automatically searches
    search_bar.send_keys(cardToSearch)

    # Set up wait times for elemetns that take longer than the page to load (Currently 5 secs)
    w = WebDriverWait(driver, 5.0)
    
    # Wait up to "5.0" seconds for card listings
    try:
        listing_information = w.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "listing-info")))
    except:
    # If nothing is listed under that card name, then close the browser and create empty list
        print("\nNo cards found listed with that name.\n")
        listing_information = []
        driver.close()
        driver.quit()

    # Set up variables to use in loop for card names, urls, and prices
    count = 0
    card_URLS = []
    card_strings = [
        "{0:<15} {1:>12}".format("Meteorite", "$-.--"),
        "{0:<15} {1:>12}".format("Shadow", "$-.--"),
        "{0:<15} {1:>12}".format("Gold", "$-.--"),
        "{0:<15} {1:>12}".format("Diamond", "$-.--"),
    ]
    # Check if any cards were listed with that name
    if (listing_information != []):
        print("\nCard Name: {0}\n".format(cardToSearch))
    # For every card found, and listed
        for item in listing_information:
    # Simulate click to open card details
            item.click()
    # Add url to url list
            card_URLS.append(driver.current_url)
    # Set up wait times for prices
            w = WebDriverWait(driver, 10.0)
    # Get cards Meta data
            meta_data = w.until(EC.presence_of_element_located((By.CLASS_NAME, "order-details-metadata")))
            meta_data_rows = meta_data.find_elements(By.CLASS_NAME, "order-details-row")
            card_quality = meta_data_rows[2].find_element(By.CLASS_NAME, "order-details-value")
            price_table = w.until(EC.presence_of_element_located((By.CLASS_NAME, "ReactTable")))
            price_row = w.until(EC.presence_of_element_located((By.CLASS_NAME, "secondary-price-col")))
    # Match card prices to their respective rarities
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
    # Print out card rarity and respectve price
        for string in card_strings:
            print(string)
    # Close out the chrome driver
        driver.close()
        driver.quit()
    
    # Prompt user to search for a new card
    cardToSearch = input("\nEnter Card Name: ")
    
    
    


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

print("\nApplication closed. You may close the terminal now.\nHave a wonderful day!\n")