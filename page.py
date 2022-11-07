from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from locator import MainPageLocators
from url import Url


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def button_accept_cookies(self):
        button_accept_choices = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ACCEPT_COOKIES)
        )
        button_accept_choices.click()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(MainPageLocators.ACCEPT_COOKIES)
        )

    def button_cookies_close(self):
        button_close = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.CLOSE_COOKIES)
        )
        button_close.click()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(MainPageLocators.ACCEPT_COOKIES)
        )



    def button_x(self):
        button_close = WebDriverWait(self.driver, 50).until(
           EC.presence_of_element_located(MainPageLocators.X_BUTTON)
        )
        button_close.click()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(MainPageLocators.DISAPPEAR_X_BUTTON)
        )



    def is_title_matches(self):
        return "Pizza Fan" in self.driver.title

    def button_log_in(self):
        log_in = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOG_IN_BUTTON)
        )
        log_in.click()


    def register(self):
        reg = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(MainPageLocators.REGISTER_BUTTON)
        )
        reg.click()

    def choice_pizzas(self):
        choice_piz = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.PIZZAS_CHOICE)
        )
        choice_piz.click()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(Url.PIZZAS)
        )
        # Wait for cookie animation to finish
        sleep(0.5)

    def title_pizzas(self):
        return "Πίτσες" in self.driver.title

    def begin_here_pizza(self):
        begin_here = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.BEGIN_PIZZA)
        )
        begin_here.click()

    def title_my_pizza(self):
        return "Φτιάξε την Πίτσα σου" in self.driver.title













