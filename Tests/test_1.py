from selenium import webdriver
import time
import unittest
from  Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Utils.locators import Locators


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../driver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        driver.get(Locators.BASE_URL)
        time.sleep(5)

        login = LoginPage(driver)
        login.enter_username(Locators.USERNAME)
        login.enter_password(Locators.PASSWORD)
        login.click_login()
        time.sleep(10)


        homepage = HomePage(driver)
        homepage.write_for_post("just for testing")
        homepage.click_twitte_button()

        # time.sleep(5)
        # self.driver.find_element_by_xpath("//input[@name='session[username_or_email]']").send_keys("01891794390")
        # self.driver.find_element_by_xpath("//input[@name='session[password]']").send_keys("Shozib_079")
        # self.driver.find_element_by_xpath("//div[@class='css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-1qd0xha r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']").click()

        time.sleep(2)

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Ok")




