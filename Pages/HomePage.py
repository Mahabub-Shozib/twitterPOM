from Utils.locators import Locators
class HomePage():
    def __init__(self, driver):
        self.driver = driver

        self.twitter_post_field_xpath = Locators.twitter_post_field_xpath
        self.twitte_button_xpath = Locators.twitte_button_xpath
    def write_for_post(self,text):
        self.driver.find_element_by_xpath(self.twitter_post_field_xpath).send_keys(text)

    def click_twitte_button(self):
        self.driver.find_element_by_xpath(self.twitte_button_xpath).click()
