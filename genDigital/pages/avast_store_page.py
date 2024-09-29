from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

class AvastStorePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Locators for SecureLine VPN and AntiTrack
    secureline_vpn_prices_locator = (By.XPATH,
                                     "//div[contains(@class, 'h5') and contains(text(), 'SecureLine VPN')]/following::div[@data-role='price']//span[@class='price-wrapper']")
    antitrack_prices_locator = (By.XPATH,
                                "//div[contains(@class, 'h5') and contains(text(), 'AntiTrack')]/following::div[@data-role='price']//span[@class='price-wrapper']")

    # Subscribe button locators for SecureLine VPN and AntiTrack
    secureline_vpn_subscribe_locator = (By.XPATH, "//a[@data-product-id='SMP-01']//span[text()='Subscribe now']")
    antitrack_subscribe_button_locator_1 = (By.XPATH, "//a[@data-product-id='APW-00']//span[text()='Subscribe now']")
    antitrack_subscribe_button_locator_2 = (By.XPATH, "//a[@data-product-id='BGW-00']//span[text()='Subscribe now']")

    cart_price_locator = (By.XPATH, "//span[@class='t-priceTable_total']/span")

    def open_avast_store(self):
        logging.info("Opening Avast store...")
        self.driver.get("https://www.avast.com/en-gb/store#pc")
        self.wait.until(EC.presence_of_element_located(self.secureline_vpn_prices_locator))

    def scroll_to_element(self, element):
        logging.info("Scrolling to element...")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)

    def dismiss_popups(self):
        try:
            popup_close_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Accept')]")
            popup_close_button.click()
            time.sleep(1)
            logging.info("Dismissed popup.")
        except Exception:
            pass

    def get_all_prices(self, locator):
        price_wrappers = self.wait.until(EC.presence_of_all_elements_located(locator))
        prices = []
        for wrapper in price_wrappers:
            try:
                integer_part = wrapper.find_element(By.CLASS_NAME, 'integer').text
            except:
                integer_part = ''
            try:
                decimal_part = wrapper.find_element(By.CLASS_NAME, 'decimal').text
            except:
                decimal_part = '.00'
            if integer_part:
                full_price = f"{integer_part}{decimal_part}"
                prices.append(full_price)
        logging.info(f"Extracted prices: {prices}")
        return prices

    def click_subscribe(self, locator, index):
        self.dismiss_popups()
        subscribe_buttons = self.wait.until(EC.presence_of_all_elements_located(locator))
        if index >= len(subscribe_buttons):
            logging.error(f"Index {index} is out of range for the subscribe buttons list (length {len(subscribe_buttons)}).")
            return False
        subscribe_button = subscribe_buttons[index]
        self.scroll_to_element(subscribe_button)
        logging.info(f"Clicking subscribe button for index {index}")
        self.driver.execute_script("arguments[0].click();", subscribe_button)
        return True

    def verify_cart_price(self, expected_price):
        cart_price_element = self.wait.until(EC.visibility_of_element_located(self.cart_price_locator))
        cart_price = cart_price_element.text.replace("£", "").strip()
        assert expected_price == cart_price, f"Price mismatch! Expected: {expected_price}, Found: {cart_price}"
        logging.info(f"Price verified! Expected: {expected_price}, Cart price: {cart_price}")

        # Reload the store page
        self.driver.get("https://www.avast.com/en-gb/store#pc")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'h5')]")))
        logging.info("Reloaded and navigated back to the store page.")

        return cart_price  # Return the cart price for comparison
