from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def check_imei(iimei_number):
   
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Ensures the browser window does not open
    # Set path to chromedriver as per your installation
    service = Service(ChromeDriverManager().install())
    # Open the website
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.get('http://imei.sy')
    # Find the IMEI input field and submit button
    imei_input = browser.find_element(By.ID, 'imei')
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button.searchbtn')
    # Enter the IMEI number and submit the form

    imei_input.clear()
    imei_input.send_keys(iimei_number)
    submit_button.click()
    # Wait for the result to load

    time.sleep(7)
    # Retrieve and return the result

    result = browser.find_element(By.ID, 'sts').text
    browser.quit()
    return result

# Path to the file containing IMEIs

imei_file_path = "imies.txt"
output_file_path = "imei_check_results.txt"
#  Read IMEIs from the file and check each, then write results to output file
#
# with open(imei_file_path, 'r') as file , open(output_file_path, 'a') as output_file:
#     imeisIntxt = file.readlines()
#     for oneimei in imeisIntxt:
#         oneimei = oneimei.strip()  # Remove any leading/trailing whitespace
#         if oneimei:  # Check if IMEI is not empty
#             result = check_imei(oneimei)
#             output_file.write(f"Result for IMEI {oneimei}: {result}\n")
#             print(f"Result for IMEI {oneimei} : {result} written to file \n")