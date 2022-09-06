from selenium.webdriver.common.by import By


class CheckoutPage():
    def __init__(self, driver):
        self.driver = driver

    cards = (By.CLASS_NAME, "card")
    cardTitle = (By.CLASS_NAME, "card-title")
    addBtn = (By.XPATH, "//button[contains(text(), 'Add')]")
    checkoutBtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    cartCheckOutBtn = (By.CLASS_NAME, "btn-success")

    def getCards(self):
        return self.driver.find_elements(*CheckoutPage.cards)

    def getCheckoutBtn(self):
        return self.driver.find_element(*CheckoutPage.checkoutBtn)

    def getCartCheckOutBtn(self):
        return self.driver.find_element(*CheckoutPage.cartCheckOutBtn)