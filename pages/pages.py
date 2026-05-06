from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import data


class UrbanRoutesPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_TAXI_BUTTON_LOCATOR = (By.XPATH, '//button[@class="button round"]')
    SUPPORTIVE_OPTION_LOCATOR = (By.XPATH, '(//div[@class="tcard-title"])[5]')
    PHONE_NUMBER_FIELD_LOCATOR = (By.XPATH, '(//div[@class="np-text"])[1]')
    PHONE_NUMBER_FIELD_LOCATOR_TWO = (By.ID, 'phone')
    PHONE_NEXT_BUTTON_LOCATOR = (By.XPATH, '(//button[@class="button full"])[1]')
    PAYMENT_METHOD_LOCATOR = (By.XPATH, '//div[@class="pp-text"]')
    ADD_CARD_LOCATOR = (By.XPATH, '(//div[@class="pp-title"])[2]')
    CARD_NUMBER_INPUT_LOCATOR = (By.XPATH, '//input[@class="card-input"]')
    CARD_CODE_INPUT_LOCATOR = (By.XPATH, '(//input[@class="card-input"])[2]')
    ADD_CARD_TITLE_LOCATOR = (By.XPATH, '(//div[@class="head"])[4]')
    LINK_BUTTON_LOCATOR = (By.XPATH, '(//button[@type="submit"])[3]')
    PAYMENT_METHOD_X_LOCATOR = (By.XPATH, '(//button[@class="close-button section-close"])[3]')
    DRIVER_COMMENT_INPUT_LOCATOR = (By.ID, 'comment')
    ICE_CREAM_PLUS_LOCATOR = (By.XPATH, '(//div[@class="counter-plus"])[1]')
    ORDER_BUTTON_LOCATOR = (By.XPATH, '//span[@class="smart-button-main"]')
    ICE_CREAM_NUMBER_LOCATOR = (By.XPATH, '(//div[@class="counter-value"])[1]')
    SMS_FIELD_LOCATOR = (By.XPATH, '(//label[@class="label"])[2]')
    SMS_INPUT_LOCATOR = (By.ID, 'code')
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, '(//button[@type="submit"])[2]')
    ADDED_CARD_LOCATOR = (By.XPATH, '//div[@class="pp-value-text"]')
    BLANKET_HANDKERCHIEF_LOCATOR = (By.XPATH, '(//span[@class="slider round"])[1]')
    BLANKET_HANDKERCHIEF_LOCATOR_TWO = (By.XPATH, '//input[@class="switch-input"]')
    CAR_SEARCH_LOCATOR = (By.XPATH, '//div[@class="order-header-title"]')

    def __init__(self, driver):
        self.driver = driver  # Initialize the driver

    def enter_from_location(self, from_text):
        # Enter From
        #self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)
        from_field = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.FROM_LOCATOR)
        )
        from_field.clear()
        from_field.send_keys(from_text)

    def enter_to_location(self, to_text):
        # Enter To
        #self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)
        to_field = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.TO_LOCATOR)
        )
        to_field.clear()
        to_field.send_keys(to_text)

    def click_call_taxi(self):
        WebDriverWait(self.driver, 5).until( EC.element_to_be_clickable(self.CALL_TAXI_BUTTON_LOCATOR)).click()

    def click_supportive_plan(self):
        WebDriverWait(self.driver, 5).until( EC.element_to_be_clickable(self.SUPPORTIVE_OPTION_LOCATOR)).click()

    def click_payment_method(self):
        WebDriverWait(self.driver, 5).until( EC.element_to_be_clickable(self.PAYMENT_METHOD_LOCATOR)).click()

    def click_add_card(self):
        WebDriverWait(self.driver, 5).until( EC.element_to_be_clickable(self.ADD_CARD_LOCATOR)).click()

    def click_card_number_field(self):
        WebDriverWait(self.driver, 5).until( EC.element_to_be_clickable(self.CARD_NUMBER_INPUT_LOCATOR)).click()

    def enter_card_number(self, card_number):
        WebDriverWait(self.driver, 5).until( EC.element_to_be_clickable(self.CARD_NUMBER_INPUT_LOCATOR)).send_keys(card_number)

    def click_code_number_field(self):
        WebDriverWait(self.driver, 5).until( EC.element_to_be_clickable(*self.CARD_CODE_INPUT_LOCATOR)).click()

    def enter_code_number(self, code_number):
        WebDriverWait(self.driver, 5).until( EC.element_to_be_clickable(self.CARD_CODE_INPUT_LOCATOR)).send_keys(code_number)

    def click_card_title(self):
        WebDriverWait(self.driver, 5).until( EC.element_to_be_clickable(self.ADD_CARD_TITLE_LOCATOR)).click()

    def click_link_button(self):
        WebDriverWait(self.driver, 5).until( EC.element_to_be_clickable(self.LINK_BUTTON_LOCATOR)).click()

    def click_x(self):
        WebDriverWait(self.driver, 5).until( EC.element_to_be_clickable(self.PAYMENT_METHOD_X_LOCATOR)).click()

    def enter_driver_comment(self, comment):
        self.driver.find_element(*self.DRIVER_COMMENT_INPUT_LOCATOR).send_keys(comment)

    def toggle_blanket_and_handkerchief(self):
        self.driver.find_element(*self.BLANKET_HANDKERCHIEF_LOCATOR).click()

    def order_ice_cream(self):
        self.driver.find_element(*self.ICE_CREAM_PLUS_LOCATOR).click()

    def order_taxi(self):
        self.driver.find_element(*self.ORDER_BUTTON_LOCATOR).click()

    def get_ice_cream_number(self):
       return self.driver.find_element(*self.ICE_CREAM_NUMBER_LOCATOR).text

    def confirm_comment_written(self):
      return self.driver.find_element(*self.DRIVER_COMMENT_INPUT_LOCATOR).get_attribute('value')

    def get_blanket_handkerchief_selection(self):
        return self.driver.find_element(*self.BLANKET_HANDKERCHIEF_LOCATOR_TWO).get_attribute('checked')

    def get_order_confirmation(self):
        return self.driver.find_element(*self.CAR_SEARCH_LOCATOR).is_displayed()

    def get_from_text(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_attribute('value')

    def get_to_text(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_attribute('value')

    def get_supportive_plan(self):
        return self.driver.find_element(*self.SUPPORTIVE_OPTION_LOCATOR).text




#Methods for phone testing
    def click_phone_number_field(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.PHONE_NUMBER_FIELD_LOCATOR)).click()

    def click_sms_field(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.SMS_FIELD_LOCATOR)).click()

    def enter_sms_field(self, sms):
        sms_input = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.SMS_INPUT_LOCATOR))
        # sms_input.clear()
        sms_input.send_keys(sms)

    def click_next_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.PHONE_NEXT_BUTTON_LOCATOR)).click()

    def enter_phone_number(self, phone_number):
        phone_input = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.PHONE_NUMBER_FIELD_LOCATOR_TWO))
       # phone_input.click()
        phone_input.send_keys(phone_number)

    def get_phone_number(self):
        return self.driver.find_element(*self.PHONE_NUMBER_FIELD_LOCATOR).text

    def click_confirm_button(self):
        self.driver.find_element(*self.CONFIRM_BUTTON_LOCATOR).click()

    def confirm_card_added(self):
       return self.driver.find_element(*self.ADDED_CARD_LOCATOR).text

