import time


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Utils.locators import Locators

driver = webdriver.Chrome(executable_path=Locators.CHROME_EXECUTABLE_PATH)
driver.implicitly_wait(10)
driver.maximize_window()


driver.get("https://twitter.com/login")
time.sleep(5)
driver.find_element_by_xpath("//input[@name='session[username_or_email]']").send_keys("01891794390")
driver.find_element_by_xpath("//input[@name='session[password]']").send_keys("Shozib_079")
driver.find_element_by_xpath("//div[@class='css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-1qd0xha r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']").click()

time.sleep(7)

# driver.find_element_by_xpath("//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']").send_keys("just for testing")
# driver.find_element_by_xpath("//div[@class = 'css-18t94o4 css-1dbjc4n r-urgr8i r-42olwf r-sdzlij r-1phboty r-rs99b7 r-19u6a5r r-ero68b r-vkv6oe r-1ny4l3l r-1fneopy r-o7ynqc r-6416eg r-lrvibr']").click()
# driver.get("https://twitter.com/search")
# time.sleep(2)
driver.find_element_by_xpath("//input[@class = 'r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-xyw6el r-y0fyvk r-1dz5y72 r-fdjqy7 r-13qz1uu']").send_keys('@TamaraWhitee' + Keys.ENTER)
time.sleep(5)
driver.find_element_by_xpath("//div[text()='People']").click()
time.sleep(2)
# check = driver.find_element_by_xpath("//div[@class='css-18t94o4 css-1dbjc4n r-1niwhzg r-p1n3y5 r-sdzlij r-1phboty r-rs99b7 r-15ysp7h r-4wgw6l r-1ny4l3l r-1fneopy r-o7ynqc r-6416eg r-lrvibr']").get_attribute("aria-label")

name = '@TamaraWhitee'
follow = driver.find_elements_by_xpath("//div[@aria-label='Follow "+name+"']")
# o = driver.find_element_by_xpath("//div[@aria-label='Following "+name+"']")
# f = check.text

# "//option[@value='" + state + "']"
# print(check)

# if driver.find_element_by_xpath("//div[@aria-label='Follow "+name+"']").is_displayed():
#    driver.find_element_by_xpath("//div[@aria-label='Follow "+name+"']").click()
#
# else:
#     print("Okay")
    # driver.find_element_by_xpath("//div[@aria-label='Following "+name+"']").click()

# elif o.is_enabled():
#     print("This guy is already followed by you!")
print("done!")


# TODo try
if len(follow) > 0:
    follow[0].click()
time.sleep(5)
driver.close()
driver.quit()