import unittest
import logging
import os
from driver.driver_setup import DriverSetup
from pages.avast_store_page import AvastStorePage
from utils.video_recorder import ScreenRecorder
from config.config import Config

class TestNavigation(unittest.TestCase):
    def setUp(self):
        self.driver = DriverSetup.get_driver()
        self.store_page = AvastStorePage(self.driver)

        # Check and create 'output' directory if it doesn't exist
        if not os.path.exists("output"):
            os.makedirs("output")

        # Initialize screen recorder
        self.recorder = ScreenRecorder(output_filename="output/avast_store_test_recording.mp4")
        self.result_file = open("output/price_comparison_results.txt", "w")

        # Start recording
        self.recorder.start_recording()

    def test_navigation_and_price_comparison(self):
        self.store_page.open_avast_store()

        # SecureLine VPN Price Comparison
        secureline_vpn_prices = self.store_page.get_all_prices(self.store_page.secureline_vpn_prices_locator)
        for index, price in enumerate(secureline_vpn_prices[:3]):  # Limit to first 3 VPN prices
            clicked = self.store_page.click_subscribe(self.store_page.secureline_vpn_subscribe_locator, index)
            if clicked:
                cart_price = self.store_page.verify_cart_price(price)
                self.result_file.write(f"SecureLine VPN: Main Page Price: {price}, Cart Page Price: {cart_price}\n")
                self.recorder.capture_frame()

        # AntiTrack Price Comparison
        antitrack_prices = self.store_page.get_all_prices(self.store_page.antitrack_prices_locator)[:2]  # Limit to first 2 AntiTrack prices
        for index, price in enumerate(antitrack_prices):
            locator = (
                self.store_page.antitrack_subscribe_button_locator_1
                if index == 0
                else self.store_page.antitrack_subscribe_button_locator_2
            )
            clicked = self.store_page.click_subscribe(locator, 0)  # Always use index 0 since each locator is unique
            if clicked:
                cart_price = self.store_page.verify_cart_price(price)
                self.result_file.write(f"AntiTrack: Main Page Price: {price}, Cart Page Price: {cart_price}\n")
                self.recorder.capture_frame()

    def tearDown(self):
        self.recorder.stop_recording()
        self.result_file.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
