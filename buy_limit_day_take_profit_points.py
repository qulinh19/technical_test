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

# Step 3: Click Buy
click_by_x_path("data-testid", "trade-button-order-buy")

# Step 4: Select Order Type: Limit
click_by_x_path("data-testid",'trade-dropdown-order-type')
click_by_x_path("data-testid",'trade-dropdown-order-type-limit')

# Step 5: Input Size
input_by_x_path("data-testid",'trade-input-volume','0.02')

# Step 6: Input Price
input_by_x_path("data-testid",'trade-input-price','0.8')

# Step 6: Input Take Profit Points
input_by_x_path("data-testid",'trade-input-takeprofit-points','10')

# Step 7: Select Expiry: Good Till Day
click_by_x_path("data-testid",'trade-dropdown-expiry')
click_by_x_path("data-testid",'trade-dropdown-expiry-good-till-day')

# Step 8: Place Buy Order
click_by_x_path("data-testid", "trade-button-order")

# Step 0: Retrieve Trade Confirmation Details
trade_confirmation = find_el_by_x_path("class", "sc-ur24yu-1 snrF")
time.sleep(2)

trade_confirmation_details = {
    "symbol": trade_confirmation.find_element(By.XPATH, "//*[@data-testid='trade-confirmation-symbol']").text,
    "type": trade_confirmation.find_element(By.XPATH, "//*[@data-testid='trade-confirmation-order-type']").text,
    "size": trade_confirmation.find_element(By.XPATH, "(//*[@data-testid='trade-confirmation-value'])[1]").text,
    "price": trade_confirmation.find_element(By.XPATH, "(//*[@data-testid='trade-confirmation-value'])[3]").text,
    "stop_loss": trade_confirmation.find_element(By.XPATH, "(//*[@data-testid='trade-confirmation-value'])[4]").text,
    "take_profit": trade_confirmation.find_element(By.XPATH, "(//*[@data-testid='trade-confirmation-value'])[5]").text,
    "expiry": trade_confirmation.find_element(By.XPATH, "(//*[@data-testid='trade-confirmation-value'])[6]").text,    
}

# Step 10: Comfirm order
click_by_x_path("data-testid","trade-confirmation-button-confirm")

# Step 11: Retrieve Toast Message Details
toast_message = find_el_by_x_path("class", "sc-1q2cym3-5 hWtVB")
time.sleep(2)

toast_message_details = {
    "symbol": toast_message.find_element(By.XPATH, "//*[@data-testid='notification-description']").text,
    "type": toast_message.find_element(By.XPATH, "//*[@data-testid='notification-description']").text,
    "size": toast_message.find_element(By.XPATH, "//*[@data-testid='notification-description']").text,
    "price": toast_message.find_element(By.XPATH, "//*[@data-testid='notification-description']").text,
    "take_profit": toast_message.find_element(By.XPATH, "//*[@data-testid='notification-description']").text
}

# Step 12: Compare Trade Confirmation Deatails and Toast Message Details
assert trade_confirmation_details["symbol"] in trade_confirmation_details["symbol"]
assert trade_confirmation_details["type"] in trade_confirmation_details["type"]
assert trade_confirmation_details["size"] in trade_confirmation_details["size"]
assert trade_confirmation_details["price"] in trade_confirmation_details["price"]
assert trade_confirmation_details["take_profit"] in trade_confirmation_details["take_profit"]


# Step 13: Minimize Symbol and Order Placing Window (if applicable)
click_by_x_path("class", "sc-j0b7z7-5 iaMuCb")

# Step 14: Open Pending Orders Details
click_by_x_path("data-testid", "tab-asset-order-type-pending-orders")

# Step 15: Retrieve Pending Orders Details
pending_orders = find_el_by_x_path("data-testid", "tab-asset-order-type-open-positions")
time.sleep(2)

pending_orders_details = {
    "open_date": pending_orders.find_element(By.XPATH, "//*[@data-testid='asset-pending-column-open-date']").text,
    "order_no": pending_orders.find_element(By.XPATH, "//*[@data-testid='asset-pending-column-order-id']").text,
    "type": pending_orders.find_element(By.XPATH, "//*[@data-testid='asset-pending-column-order-type']").text,
    "size": pending_orders.find_element(By.XPATH, "//*[@data-testid='asset-pending-column-volume']").text,
    "units": pending_orders.find_element(By.XPATH, "//*[@data-testid='asset-pending-column-units']").text,
    "expiry": pending_orders.find_element(By.XPATH, "//*[@data-testid='asset-pending-column-expiry']").text,
    "price": pending_orders.find_element(By.XPATH, "//*[@data-testid='asset-pending-column-entry-price']").text,
    "current_price": pending_orders.find_element(By.XPATH, "//*[@data-testid='asset-pending-column-current-price']").text,
    "take_profit": pending_orders.find_element(By.XPATH, "//*[@data-testid='asset-pending-column-take-profit']").text,
    "stop_loss": pending_orders.find_element(By.XPATH, "//*[@data-testid='asset-pending-column-stop-loss']").text,
}

# Step 16: Compare Trade Confirmation Deatails and Pending Orders Details
assert trade_confirmation_details["type"] in pending_orders_details["type"]
assert trade_confirmation_details["size"] in pending_orders_details["size"]
assert trade_confirmation_details["price"] in pending_orders_details["price"]
assert trade_confirmation_details["expiry"] in pending_orders_details["expiry"]
assert trade_confirmation_details["stop_loss"] in pending_orders_details["stop_loss"]
assert trade_confirmation_details["take_profit"] in pending_orders_details["take_profit"]