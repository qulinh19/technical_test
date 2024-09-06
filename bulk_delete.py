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

# Step 4: Open Pending Orders Details
click_by_x_path("data-testid", "tab-asset-order-type-pending-orders")
time.sleep(1)

# Step 5: Select Bulk Delete
click_by_x_path("data-testid",'bulk-delete')

# Step 6: Retrieve Bulk Delete Confirmation
bulk_delete_confirmation = find_el_by_x_path("class", "sc-xjowud-0 jLpeil")
time.sleep(2)

bulk_delete_confirmation_details = {
    "bulk_delete": bulk_delete_confirmation.find_element(By.XPATH, "//*[@class='sc-b0kd5b-1 sc-1n2p8w2-2 dAKLOq kGAeGw']").text,
    "maximum_delete": bulk_delete_confirmation.find_element(By.XPATH, "//*[@class='sc-1n2p8w2-3 IYaCP']").text,
    "confirmation_message": bulk_delete_confirmation.find_element(By.XPATH, "//*[@class='sc-1n2p8w2-5 dzDzgj']").text,
    "cancel": bulk_delete_confirmation.find_element(By.XPATH, "//*[@class='sc-88z1lo-0 bpBnKZ large stretch']").text,
    "confirm": bulk_delete_confirmation.find_element(By.XPATH, "//*[@class='sc-88z1lo-0 cElBaW large stretch']").text
}

# Step 7: Compare Bulk Close Confirmation
assert bulk_delete_confirmation_details["bulk_delete"].strip() == "Bulk Delete"
assert bulk_delete_confirmation_details["maximum_delete"].strip() == "Note: A maximum of 30 pending orders will be deleted."
assert bulk_delete_confirmation_details["confirmation_message"].strip() == "Would you like to delete the AUDCAD.std pending orders?"
assert bulk_delete_confirmation_details["cancel"].strip() == "Cancel"
assert bulk_delete_confirmation_details["confirm"].strip() == "Confirm"

# Step 8: Click Confirm
click_by_x_path("class",'sc-88z1lo-0 cElBaW large stretch')


# Step 9: Retrieve Toast Message Details
toast_message = find_el_by_x_path("class", "sc-1q2cym3-5 hWtVB")

toast_message_details = {
    "title": toast_message.find_element(By.XPATH, "//*[@class='sc-1q2cym3-6 ffciB']").text,
    "description": toast_message.find_element(By.XPATH, "//*[@data-testid='notification-description']").text,
}

# Step 10: Compare Toast Message Details
assert toast_message_details["title"].strip() == "Bulk deletion of pending orders"
assert "Pending orders have been deleted." in toast_message_details["description"].strip()
