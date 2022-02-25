import os
# from typing import Any

from selenium import webdriver
from selenium.webdriver.common.by import By

import booking.booking_filtration as BookingFiltration


class Booking(webdriver.Chrome):
    def __init__(self,
                 driver_path: str = '/Users/gotaaibara/Documents/selenium_driver/chromedriver',
                 teardown: bool = False
                 ) -> None:
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        self.teardown = teardown
        super(Booking, self).__init__(self.driver_path)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self) -> None:
        self.get('https://www.booking.com/')

    def change_currency(self, currency : str = None) -> None:
        currency_element = self.find_element(
            By.CSS_SELECTOR,
            'button[data-modal-header-async-type="currencyDesktop"]') #data-tooltip-text="表示通貨を選択"
        currency_element.click()
        selected_currency_element = self.find_element(
            By.CSS_SELECTOR,
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go: str = None) -> None:
        serach_field = self.find_element(By.ID, 'ss')
        serach_field.clear()
        serach_field.send_keys(place_to_go)
        first_result = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        first_result.click()

    def select_dates(self, check_in_date: str, check_out_date: str) -> None:
        check_in_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]')
        check_in_element.click()
        check_out_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out_date}"]')
        check_out_element.click()

    def select_adults(self, count: int = 1) -> None:
        selection_element = self.find_element(By.ID, 'xp__guests__toggle')
        selection_element.click()

        while True:
            decrease_adults_element = self.find_element(
                By.XPATH,
                '//*[@id="xp__guests__inputs-container"]/div/div/div[1]/div/div[2]/button[1]')
            decrease_adults_element.click()

            adults_value_element = self.find_element(By.ID, 'group_adults')
            adults_value = adults_value_element.get_attribute('value') # 表示されている大人の人数を数える
            if int(adults_value) == 1:
                break

        increase_adults_element = self.find_element(
                By.XPATH,
                '//*[@id="xp__guests__inputs-container"]/div/div/div[1]/div/div[2]/button[2]')

        for _ in range(count - 1):
            increase_adults_element.click()


    def select_rooms(self, count: int = 1) -> None:
        selection_element = self.find_element(By.ID, 'xp__guests__toggle')
        selection_element.click()

        rooms_value_element = self.find_element(By.ID, 'no_rooms')
        rooms_value = rooms_value_element.get_attribute('value') # 表示されている大人の人数を数える

        if int(rooms_value) > 1:
            while True:
                decrease_rooms_element = self.find_element(
                    By.XPATH,
                    '//*[@id="xp__guests__inputs-container"]/div/div/div[4]/div/div[2]/button[1]')
                decrease_rooms_element.click()
                rooms_value = rooms_value_element.get_attribute('value')
                if int(rooms_value) == 1:
                    break

        increase_rooms_element = self.find_element(
                By.XPATH,
                '//*[@id="xp__guests__inputs-container"]/div/div/div[4]/div/div[2]/button[2]')

        if count > 30:
            count = 30

        for _ in range(count - 1):
            increase_rooms_element.click()

    def click_search(self) -> None:
        search_button = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        search_button.click()

    def apply_filtrations(self) -> None:
        filtration = BookingFiltration(driver=self)