from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from login import login_to_trade_page
from web_driver import wait, driver
from utils import find_el_by_x_path, click_by_x_path, input_by_x_path

# Step 1: Login to WT
login_to_trade_page("188889346","$w7h06b#3ZXS")

# Step 2: Search for a Stock Symbol
stock_symbol = "AUDCAD.std"
search_box = find_el_by_x_path("data-testid",'symbol-input-search')
search_box.send_keys(stock_symbol)
time.sleep(2)
click_by_x_path("data-testid","symbol-input-search-items")
time.sleep(1)

# Step 3: Minimize Symbol and Order Placing Window (if applicable)
wait.until(EC.visibility_of_element_located((By.XPATH, "(//*[@class='sc-j0b7z7-5 iaMuCb'])[1]"))).click()
wait.until(EC.visibility_of_element_located((By.XPATH, "(//*[@class='sc-j0b7z7-5 iaMuCb'])[2]"))).click()

# Step 4: Retrieve Open Positions Order Details
open_positions = find_el_by_x_path("data-testid", "tab-asset-order-type-open-positions")

# Step 5: Select Close button
click_by_x_path("data-testid",'asset-open-button-close')

# Step 7: Retrieve Partial Close Confirmation
partial_close_confirmation = find_el_by_x_path("class", "sc-xjowud-0 jLpeil")
time.sleep(2)

partial_close_confirmation_details = {
    "confirmation_message": partial_close_confirmation.find_element(By.XPATH, "//*[@class='sc-b0kd5b-1 sc-hvvxec-0 dAKLOq bggmGI']").text,
    "symbol": partial_close_confirmation.find_element(By.XPATH, "//*[@class='sc-hvvxec-1 fzGQLP']").text,
    "cancel": partial_close_confirmation.find_element(By.XPATH, "//*[@data-testid='close-order-cancel']").text,
    "close_order": partial_close_confirmation.find_element(By.XPATH, "//*[@data-testid='close-button-submit']").text
}

# Step 9: Compare Bulk Close Confirmation
assert partial_close_confirmation_details["confirmation_message"].strip() == "Confirm Close Order?"
assert partial_close_confirmation_details["symbol"].strip() == "AUDCAD.std"
assert partial_close_confirmation_details["cancel"].strip() == "Cancel"
assert partial_close_confirmation_details["close_order"].strip() == "Close Order"

# Step 5: Decrease Size
click_by_x_path("data-testid",'close-order-input-volume-decrease')

# Step 5: Click Close Order
click_by_x_path("data-testid",'close-button-submit')


# Step 9: Retrieve Toast Message Details
toast_message = find_el_by_x_path("class", "sc-1q2cym3-0 QzDQO")

toast_message_details = {
    "title": toast_message.find_element(By.XPATH, "//*[@data-testid='notification-title']").text,
    "description": toast_message.find_element(By.XPATH, "//*[@data-testid='notification-description']").text,
}

# Step 9: Compare Toast Message Details
assert toast_message_details["title"].strip() == "Close Order"
assert toast_message_details["description"].strip() == "AUDCAD.std - Buy order closed successfully."
