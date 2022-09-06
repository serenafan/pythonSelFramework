from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage():
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[contains(@href, 'shop')]")
    emailField = (By.NAME, "email")
    nameField = (By.CSS_SELECTOR, "input[name='name']")
    submitBtn = (By.XPATH, "//input[@type ='submit']")
    successMsg = (By.CLASS_NAME, "alert-success")
    passwordField = (By.ID, "exampleInputPassword1")

    def shopItem(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckoutPage(self.driver)
        return checkOutPage

    def getEmailField(self):
        return self.driver.find_element(*HomePage.emailField)

    def getNameField(self):
        return self.driver.find_element(*HomePage.nameField)

    def getSubmitBtn(self):
        return self.driver.find_element(*HomePage.submitBtn)

    def getSuccessMsg(self):
        return self.driver.find_element(*HomePage.successMsg)

    def getPasswordField(self):
        return self.driver.find_element(*HomePage.passwordField)
