import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        self.driver.get("http://rahulshettyacademy.com/angularpractice/")
        log.info("click on shop item")
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItem()


        log.info("add all products to card")
        cards = checkOutPage.getCards()
        for card in cards:
            if "Blackberry" in card.find_element(*checkOutPage.cardTitle).text:
                card.find_element(*checkOutPage.addBtn).click()

        log.info("checkout the items")
        checkOutPage.getCheckoutBtn().click()
        checkOutPage.getCartCheckOutBtn().click()


        self.driver.find_element(By.ID, "country").send_keys("Ind")
        self.waitLinkPresence("India")

        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.CLASS_NAME, "checkbox-primary").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        log.info("text recilved from application" + self.driver.find_element(By.CLASS_NAME, "alert-success").text)

        assert "Success3333" in self.driver.find_element(By.CLASS_NAME, "alert-success").text
