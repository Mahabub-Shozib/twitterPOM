import time

from Utils.locators import Locators
from selenium.webdriver.common.keys import Keys


class FollowPage():
    def __init__(self, driver):
        self.driver = driver

        self.twitter_search_bar_xpath = Locators.twitter_search_bar
        self.twitte_people_page_xpath = Locators.people_page

    def follow_people(self,name):
        self.driver.find_element_by_xpath(self.twitter_search_bar_xpath).send_keys(name + Keys.ENTER)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.twitte_people_page_xpath).click()
        time.sleep(2)
        follow = self.driver.find_elements_by_xpath("//div[@aria-label='Follow "+name+"']")
        if len(follow) > 0:
            follow[0].click()
