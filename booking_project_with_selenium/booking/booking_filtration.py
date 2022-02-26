import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    """filtering search results getting with booking.com"""
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def apply_star_rating(self, *star_values) -> None:
        star_filtration_box = self.driver.find_element(By.CSS_SELECTOR, 'div[data-filters-group="class"]')
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, '*')

        for star_value in star_values:

            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value}つ星': # change japanese rating sentence つ星 to your language.
                    star_element.click()


    def sort_price_lowest_filter(self) -> None:
        time.sleep(1)
        element = self.driver.find_element(By.CSS_SELECTOR, 'li[data-id="price"]')
        element.click()
