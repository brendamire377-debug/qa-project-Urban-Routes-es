
from data import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.urban_routes_pages import UrbanRoutesPage


class TestUrbanRoutes:

    def setup_method(self):
        options = Options()
        options.set_capability("goog:loggingPrefs",{'performance':'ALL'})
        self.driver = webdriver.Chrome(service=Service(), options=options)
        self.driver.get(data.urban_routes_url)
        self.routes_page = UrbanRoutesPage(self.driver)

    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_2_select_comfort_tariff(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.select_comfort_tariff()
        assert self.routes_page.get_comfort_icon_assert() == 'Comfort'

    def test_3_fill_phone_number(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.select_comfort_tariff()
        self.routes_page.set_phone_number(data.phone_number)
        assert self.routes_page.get_phone_number() == data.phone_number

    def test_4_add_card_number(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.select_comfort_tariff()
        self.routes_page.set_phone_number(data.phone_number)
        self.routes_page.set_card_number(data.card_number,data.card_code)
        assert self.routes_page.get_card_number() == 'Tarjeta'

    def test_5_message_for_driver(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.select_comfort_tariff()
        self.routes_page.set_phone_number(data.phone_number)
        self.routes_page.set_card_number(data.card_number,data.card_code)
        self.routes_page.write_message_for_driver(data.message_for_driver)
        assert self.routes_page.get_message_for_driver() == data.message_for_driver

    def test_6_request_blanket_and_kerchief(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.select_comfort_tariff()
        self.routes_page.set_phone_number(data.phone_number)
        self.routes_page.set_card_number(data.card_number,data.card_code)
        self.routes_page.write_message_for_driver(data.message_for_driver)
        self.routes_page.request_blanket_and_kerchief()
        assert self.routes_page.request_blanket_and_kerchief_status() == 'Has seleccionado manta y pañuelos'

    def test_7_ice_cream(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.select_comfort_tariff()
        self.routes_page.set_phone_number(data.phone_number)
        self.routes_page.set_card_number(data.card_number,data.card_code)
        self.routes_page.write_message_for_driver(data.message_for_driver)
        self.routes_page.request_blanket_and_kerchief()
        self.routes_page.request_ice_cream()
        assert self.routes_page.request_ice_cream_counter() == '2'

    def test_8_look_for_taxi(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.select_comfort_tariff()
        self.routes_page.set_phone_number(data.phone_number)
        self.routes_page.set_card_number(data.card_number, data.card_code)
        self.routes_page.write_message_for_driver(data.message_for_driver)
        self.routes_page.request_blanket_and_kerchief()
        self.routes_page.request_ice_cream()
        self.routes_page.look_for_taxi()
        assert self.routes_page.look_for_taxi_appear() == 'Aparece modal'


    def teardown_method(self):
        self.driver.quit()
