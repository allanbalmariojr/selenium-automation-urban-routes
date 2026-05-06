import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage


class TestUrbanRoutes:
    # Task 4
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}

        cls.driver = webdriver.Chrome()

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes Server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    # Task 3
    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        actual_value_from = urban_routes_page.get_from_text()
        expected_value_from = data.ADDRESS_FROM
        assert expected_value_from == actual_value_from
        actual_value_to = urban_routes_page.get_to_text()
        expected_value_to = data.ADDRESS_TO
        assert expected_value_to == actual_value_to

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_call_taxi()
        urban_routes_page.click_supportive_plan()
        assert urban_routes_page.get_supportive_plan() == data.PLAN_CONFIRMATION

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_call_taxi()
        urban_routes_page.click_supportive_plan()
        urban_routes_page.click_phone_number_field()
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        urban_routes_page.click_next_button()
        sms = helpers.retrieve_phone_code(self.driver)
        urban_routes_page.enter_sms_field(sms)
        urban_routes_page.click_confirm_button()
        actual_value = urban_routes_page.get_phone_number()
        expected_value = data.PHONE_NUMBER
        assert expected_value == actual_value

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_call_taxi()
        urban_routes_page.click_payment_method()
        urban_routes_page.click_add_card()
        urban_routes_page.enter_card_number(data.CARD_NUMBER)
        urban_routes_page.enter_code_number(data.CARD_CODE)
        urban_routes_page.click_card_title()
        urban_routes_page.click_link_button()
        urban_routes_page.click_x()
        actual_value = urban_routes_page.confirm_card_added()
        expected_value = data.CARD_CONFIRMATION
        assert expected_value == actual_value

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_call_taxi()
        urban_routes_page.enter_driver_comment(data.MESSAGE_FOR_DRIVER)
        actual_value = urban_routes_page.confirm_comment_written()
        expected_value = data.MESSAGE_FOR_DRIVER
        assert expected_value == actual_value

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_call_taxi()
        urban_routes_page.click_supportive_plan()
        urban_routes_page.toggle_blanket_and_handkerchief()
        assert urban_routes_page.get_blanket_handkerchief_selection()

    # Task 5
    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_call_taxi()
        urban_routes_page.click_supportive_plan()
        for number in range(0, 2):
            urban_routes_page.order_ice_cream()
        actual_value = urban_routes_page.get_ice_cream_number()
        expected_value = data.ICE_CREAM_CONFIRMATION
        assert expected_value == actual_value

    def test_car_search_model(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_from_location(data.ADDRESS_FROM)
        urban_routes_page.enter_to_location(data.ADDRESS_TO)
        urban_routes_page.click_call_taxi()
        urban_routes_page.click_supportive_plan()
        urban_routes_page.click_phone_number_field()
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        urban_routes_page.click_next_button()
        sms = helpers.retrieve_phone_code(self.driver)
        urban_routes_page.enter_sms_field(sms)
        urban_routes_page.click_confirm_button()
        urban_routes_page.click_payment_method()
        urban_routes_page.click_add_card()
        urban_routes_page.enter_card_number(data.CARD_NUMBER)
        urban_routes_page.enter_code_number(data.CARD_CODE)
        urban_routes_page.click_card_title()
        urban_routes_page.click_link_button()
        urban_routes_page.click_x()
        urban_routes_page.enter_driver_comment(data.MESSAGE_FOR_DRIVER)
        urban_routes_page.order_taxi()
        actual_value = urban_routes_page.get_order_confirmation()
        expected_value = data.CAR_ORDER_CONFIRMATION
        assert expected_value == actual_value

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()