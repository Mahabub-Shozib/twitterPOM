class Locators():

    ## Driver path
    CHROME_EXECUTABLE_PATH = "../driver/chromedriver.exe"

    ##------credentials---------
    BASE_URL = "https://twitter.com/login"
    USERNAME = "01891794390"
    PASSWORD = "Shozib_079"

    ## LoginPage
    username_textbox_xpath = "//input[@name='session[username_or_email]']"
    password_textbox_xpath = "//input[@name='session[password]']"
    login_button_xpath = "//div[@class='css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-1qd0xha r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']"

    ## HomePage
    twitter_post_field_xpath = "//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']"
    twitte_button_xpath = "//div[@class = 'css-18t94o4 css-1dbjc4n r-urgr8i r-42olwf r-sdzlij r-1phboty r-rs99b7 r-19u6a5r r-ero68b r-vkv6oe r-1ny4l3l r-1fneopy r-o7ynqc r-6416eg r-lrvibr']"

    ##For follow
    twitter_search_bar = "//input[@class = 'r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-xyw6el r-y0fyvk r-1dz5y72 r-fdjqy7 r-13qz1uu']"
    people_page = "//div[text()='People']"
    follow_button_check = "//div[@class='css-18t94o4 css-1dbjc4n r-1niwhzg r-p1n3y5 r-sdzlij r-1phboty r-rs99b7 r-15ysp7h r-4wgw6l r-1ny4l3l r-1fneopy r-o7ynqc r-6416eg r-lrvibr']"


