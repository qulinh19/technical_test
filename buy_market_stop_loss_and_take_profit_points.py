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

# Step 4: Select Order Type Market
click_by_x_path("data-testid",'trade-dropdown-order-type')
click_by_x_path("data-testid",'trade-dropdown-order-type-market')

# Step 5: Input Size
input_by_x_path("data-testid",'trade-input-volume','0.02')

# Step 6: Input Stop Loss Points
input_by_x_path("data-testid",'trade-input-stoploss-points','123')

# Step 7: Input Take Profit Points
input_by_x_path("data-testid", 'trade-input-takeprofit-points', '1234')

# Step 8: Place Buy Order
click_by_x_path("data-testid", "trade-button-order")

# Step 9: Retrieve Trade Confirmation Details
trade_confirmation = find_el_by_x_path("class", "sc-ur24yu-1 snrF")
time.sleep(2)

trade_confirmation_details = {
    "symbol": trade_confirmation.find_element(By.XPATH, "//*[@data-testid='trade-confirmation-symbol']").text,
    "type": trade_confirmation.find_element(By.XPATH, "//*[@data-testid='trade-confirmation-order-type']").text,
    "size": trade_confirmation.find_element(By.XPATH, "(//*[@data-testid='trade-confirmation-value'])[1]").text,
    "stop_loss": trade_confirmation.find_element(By.XPATH, "(//*[@data-testid='trade-confirmation-value'])[2]").text,
    "take_profit": trade_confirmation.find_element(By.XPATH, "(//*[@data-testid='trade-confirmation-value'])[3]").text
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
    "stop_loss": toast_message.find_element(By.XPATH, "//*[@data-testid='notification-description']").text,
    "take_profit": toast_message.find_element(By.XPATH, "//*[@data-testid='notification-description']").text
}

# Step 12: Compare Trade Confirmation Deatails and Toast Message Details
assert trade_confirmation_details["symbol"] in toast_message_details["symbol"]
assert trade_confirmation_details["type"] in toast_message_details["type"]
assert trade_confirmation_details["size"] in toast_message_details["size"]
assert trade_confirmation_details["stop_loss"] in toast_message_details["stop_loss"]
assert trade_confirmation_details["take_profit"] in toast_message_details["take_profit"]

# Step 13: Minimize Symbol and Order Placing Window (if applicable)
click_by_x_path("class", "sc-j0b7z7-5 iaMuCb")

# Step 14: Retrieve Open Positions Order Details
open_positions = find_el_by_x_path("data-testid", "tab-asset-order-type-open-positions")
time.sleep(2)

open_positions_details = {
    "symbol": open_positions.find_element(By.XPATH, "//*[@data-testid='asset-open-column-open-date']").text,
    "open_date": open_positions.find_element(By.XPATH, "//*[@data-testid='asset-open-column-open-date']").text,
    "order_no": open_positions.find_element(By.XPATH, "//*[@data-testid='asset-open-column-order-id']").text,
    "type": open_positions.find_element(By.XPATH, "//*[@data-testid='asset-open-column-order-type']").text,
    "profit_loss": open_positions.find_element(By.XPATH, "//*[@data-testid='asset-open-column-profit']").text,
    "size": open_positions.find_element(By.XPATH, "//*[@data-testid='asset-open-column-volume']").text,
    "units": open_positions.find_element(By.XPATH, "//*[@data-testid='asset-open-column-units']").text,
    "entry_price": open_positions.find_element(By.XPATH, "//*[@data-testid='asset-open-column-entry-price']").text,
    "current_price": open_positions.find_element(By.XPATH, "//*[@data-testid='asset-open-column-current-price']").text,
    "take_profit": open_positions.find_element(By.XPATH, "//*[@data-testid='asset-open-column-take-profit']").text,
    "stop_loss": open_positions.find_element(By.XPATH, "//*[@data-testid='asset-open-column-stop-loss']").text,
    "swap": open_positions.find_element(By.XPATH, "//*[@data-testid='asset-open-column-swap']").text,
    "commission": open_positions.find_element(By.XPATH, "//*[@data-testid='asset-open-column-commission']").text
}

# Step 15: Compare Trade Confirmation Deatails and Open Positions Order Details
assert trade_confirmation_details["type"] in open_positions_details["type"]
assert trade_confirmation_details["size"] in open_positions_details["size"]
assert trade_confirmation_details["stop_loss"] in open_positions_details["stop_loss"]
assert trade_confirmation_details["take_profit"] in open_positions_details["take_profit"]