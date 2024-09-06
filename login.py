from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time 
from selenium.webdriver.support.ui import Select
from web_driver import wait, driver
# Set up the WebDriver (for Chrome in this case)
# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 10)

# Define the URL of the Trade page
trade_page_url = "https://www.aquariux.com/solutions/trader/"    

# Function to log in if necessary
def login_to_trade_page(username, password):
    driver.get(trade_page_url)
    driver.maximize_window()
    time.sleep(2)

    driver.find_element(By.XPATH, "(//*[@class='product-body'])/button").click()
    driver.find_element(By.XPATH, "(//*[contains(@class, 'Experience')]/button)[2]").click()
    
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@data-testid='login-user-id']"))).send_keys(username)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@data-testid='login-password']"))).send_keys(password)
    driver.find_element(By.XPATH, "//*[@data-testid='login-submit']").click()


        # Step 1: Log in
    # loginToTradePage("188889346", "$w7h06b#3ZXS")