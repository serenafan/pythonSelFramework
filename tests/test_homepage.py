import pytest
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from testData.HomePageData import HomePageData


class TestHomePage(BaseClass):
    def test_form(self, getData):
        self.driver.get("http://rahulshettyacademy.com/angularpractice/")
        homepage = HomePage(self.driver)
        homepage.getNameField().send_keys(getData["firstname"])
        homepage.getPasswordField().send_keys(getData["password"])
        homepage.getEmailField().send_keys(getData["email"])
        homepage.getSubmitBtn().click()
        assert ("success" in homepage.getSuccessMsg().text)

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
