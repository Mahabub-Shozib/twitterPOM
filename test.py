import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://twitter.com/login")
time.sleep(5)
driver.find_element_by_xpath("//input[@name='session[username_or_email]']").send_keys("01891794390")
driver.find_element_by_xpath("//input[@name='session[password]']").send_keys("Shozib_079")
driver.find_element_by_xpath("//div[@class='css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-1qd0xha r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']").click()

time.sleep(10)

driver.find_element_by_xpath("//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']").send_keys("just for testing")
driver.find_element_by_xpath("//div[@class = 'css-18t94o4 css-1dbjc4n r-urgr8i r-42olwf r-sdzlij r-1phboty r-rs99b7 r-19u6a5r r-ero68b r-vkv6oe r-1ny4l3l r-1fneopy r-o7ynqc r-6416eg r-lrvibr']").click()
time.sleep(5)
driver.close()
driver.quit()