
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.wait import WebDriverWait
from utils.retrive_code import retrieve_phone_code
from selenium.webdriver.common.keys import Keys


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_icon = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    comfort_icon_assert = (By.CSS_SELECTOR, '.tcard.active .tcard-title')
    phone_number_control = (By.CSS_SELECTOR, '.np-text')
    phone_number_field = (By.ID, "phone")
    phone_number_button_next = (By.XPATH, '//button[@class="button full" and text()="Siguiente"]' )
    phone_number_code_field = (By.ID, "code")
    phone_number_button_confirm = (By.XPATH, '//button[@class="button full" and text()="Confirmar"]')
    payment_method_select = (By.XPATH, '//div[@class="pp-text" and text()="Método de pago"]')
    add_card_select = (By.XPATH, '//div[@class="pp-title" and text()="Agregar tarjeta"]')
    add_card_number_input = (By.ID, 'number')
    add_code_card_input = (By.XPATH, '//input[@id="code" and @class="card-input"]')
    card_confirm_button = (By.XPATH, '//button[@class="button full" and text()="Agregar"]' )
    close_payment_method = (By.XPATH, '//div[@class="payment-picker open"]//button[@class= "close-button section-close"]')
    current_payment_method = (By.CSS_SELECTOR, '.pp-value-text')
    message_for_driver_control = (By.XPATH, '//label[@for="comment" and text()="Mensaje para el conductor..."]')
    message_for_driver_field = (By.ID, "comment")
    blanket_and_kerchief_switch = (By.XPATH, "//div[@class='r-sw-label' and text()='Manta y pañuelos']/following-sibling::div//span[@class='slider round']")
    blanket_and_kerchief_status = (By.XPATH,  "//div[@class='r-sw-label' and text()='Manta y pañuelos']/following-sibling::div//input[@type='checkbox']")
    add_ice_cream = (By.XPATH, "//div[@class='r-counter-label' and text()='Helado']/following-sibling::div//div[@class='counter-plus' and text()='+']" )
    add_ice_cream_counter= (By.XPATH, "//div[@class='r-counter-label' and normalize-space()='Helado']/following-sibling::div[@class='r-counter']//div[@class='counter-value']")
    look_for_taxi_button = (By.XPATH, "//div[@class='smart-button-wrapper']//button[@class='smart-button'][.//span[normalize-space()='Pedir un taxi']]")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)


    def set_from(self, from_address):
        self.wait.until(
            EC.visibility_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(
            EC.visibility_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)


    def select_comfort_tariff(self):
        self.wait.until(EC.element_to_be_clickable(self.request_taxi_button)).click()
        self.wait.until(EC.element_to_be_clickable(self.comfort_icon)).click()
    def get_comfort_icon_assert(self):
        comfort_tariff = self.wait.until(EC.visibility_of_element_located(self.comfort_icon_assert)).text
        return comfort_tariff


    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_control).click()
        self.wait.until(EC.visibility_of_element_located(self.phone_number_field)).send_keys(phone_number)
        self.driver.find_element(*self.phone_number_button_next).click()
        code=retrieve_phone_code(self.driver)
        self.driver.find_element(*self.phone_number_code_field).send_keys(code)
        self.driver.find_element(*self.phone_number_button_confirm).click()
    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number_control).text


    def set_card_number(self, card_number, card_code):
        self.driver.find_element(*self.payment_method_select).click()
        self.driver.find_element(*self.add_card_select).click()
        self.wait.until(EC.visibility_of_element_located(self.add_card_number_input)).send_keys(card_number)
        self.driver.find_element(*self.add_card_number_input).send_keys(Keys.TAB)
        self.wait.until(EC.visibility_of_element_located(self.add_code_card_input)).send_keys(card_code)
        self.driver.find_element(*self.add_code_card_input).send_keys(Keys.TAB)
        self.driver.find_element(*self.card_confirm_button).click()
        self.wait.until(EC.element_to_be_clickable(self.close_payment_method)).click()
    def get_card_number(self):
        return self.driver.find_element(*self.current_payment_method).text


    def write_message_for_driver(self, message_for_driver):
        self.wait.until(EC.presence_of_element_located(self.message_for_driver_control)).click()
        self.wait.until(EC.visibility_of_element_located(self.message_for_driver_field)).send_keys(message_for_driver)
        #self.driver.find_element(*self.message_for_driver_field).send_keys(Keys.TAB)
    def get_message_for_driver(self):
        return self.driver.find_element(*self.message_for_driver_field).get_property('value')


    def request_blanket_and_kerchief(self):
        self.wait.until(EC.element_to_be_clickable(self.blanket_and_kerchief_switch)).click()
    def request_blanket_and_kerchief_status(self):
        blanket_switch=self.driver.find_element(*self.blanket_and_kerchief_status)
        if blanket_switch.is_selected():
            blanket_switch ='Has seleccionado manta y pañuelos'
        else:
            blanket_switch = 'No has seleccionado manta y pañuelos'
        return blanket_switch


    def request_ice_cream(self):
        element_ice_cream = self.wait.until(EC.visibility_of_element_located(self.add_ice_cream))
        #driver.execute_script("arguments[0].scrollIntoView();", element_ice_cream)
        element_ice_cream.click()
        element_ice_cream.click()
    def request_ice_cream_counter(self):
        counter_ice_cream = self.wait.until(EC.presence_of_element_located(self.add_ice_cream_counter)).text
        return counter_ice_cream


    def look_for_taxi(self):
        self.wait.until(EC.element_to_be_clickable(self.look_for_taxi_button)).click()
    def look_for_taxi_appear(self):
        taxi_button = self.driver.find_element(*self.look_for_taxi_button)
        if taxi_button.is_displayed():
            taxi_button = 'Aparece modal'
        else :
            taxi_button = 'No aparece modal'
        return taxi_button







































