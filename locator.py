from selenium.webdriver.common.by import By

class MainPageLocators(object):
    ACCEPT_COOKIES = (By.CSS_SELECTOR, "#cookieButtonsContainer span:nth-child(1)")
    CLOSE_COOKIES = (By.CSS_SELECTOR, "#accept_cook button.close")
    X_BUTTON = (By.CSS_SELECTOR, "#shownEnv button.close")
    DISAPPEAR_X_BUTTON = (By.CSS_SELECTOR, "div.modal-backdrop.fade")
    LOG_IN_BUTTON = (By.CLASS_NAME, "white.PFHandbookPro.loginButton")
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".contentHolder span:nth-child(2)")
    PIZZAS_CHOICE = (By.LINK_TEXT, "Πιτσες")
    BEGIN_PIZZA = (By.CSS_SELECTOR, "#customItem button")