import time


from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from tqdm import tqdm

class BookingReport:
    def __init__(self, boxes_section_element: WebElement) -> None:
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()


    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')
        # return self.boxes_section_element.find_elements(By.CLASS_NAME, 'sr_property_block')

    def pull_deal_box_attributes(self) -> list:
        collection = []
        for deal_box in tqdm(self.deal_boxes):

            try:
                hotel_name = deal_box.find_element(
                    By.CSS_SELECTOR, 'div[data-testid="title"]'
                ).get_attribute('innerHTML').strip()
            except Exception as e:
                hotel_name = None

            price = deal_box.find_element(
                    By.CSS_SELECTOR, 'div[data-testid="price-and-discounted-price"]')

            try:
                before_discount_price = price.find_element(
                    By.CLASS_NAME, '_6b0bd403c'
                ).get_attribute('innerText')
            except Exception as e:
                discount_price = None

            try:
                hotel_price = price.find_element(
                    By.CLASS_NAME, '_e885fdc12'
                ).get_attribute('innerText')
            except Exception as e:
                hotel_price = None


            collection.append([hotel_name, before_discount_price, hotel_price])

        return collection


    def display_table(self):
        pass
