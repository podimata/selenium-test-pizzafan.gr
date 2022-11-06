import unittest
from selenium import webdriver
import page
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class PizzafanGr(unittest.TestCase):

    def setUp(self):
        options = FirefoxOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)
        self.driver.get("https://www.pizzafan.gr/el")


    def test_pizza_fan(self):
        main_page = page.MainPage(self.driver)
        self.assertTrue(main_page.is_title_matches())

    def test_pizza_fan_log_in(self):
        main_page = page.MainPage(self.driver)
        main_page.button_accept_cookies()
        main_page.button_x()
        main_page.button_log_in()

    def test_register(self):
        main_page = page.MainPage(self.driver)
        main_page.button_cookies_close()
        main_page.button_x()
        main_page.register()

    def test_choice_pizzas(self):
        main_page = page.MainPage(self.driver)
        main_page.button_cookies_close()
        main_page.button_x()
        main_page.choice_pizzas()
        self.assertTrue(main_page.title_pizzas())
        main_page.button_cookies_close()
        main_page.begin_here_pizza()
        main_page.button_cookies_close()
        self.assertTrue(main_page.title_my_pizza())

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()