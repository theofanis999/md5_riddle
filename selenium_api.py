from selenium import webdriver as webDriver
from time import sleep

class selenium_api:

    def __init__(self, url):
        self.url = url
        self.driver = webDriver.Firefox()
        self.slows = 0

    def go_to_page(self):
        self.driver.get(self.url)
        # self.check_if_i_am_slow()

    def close_browser(self):
        self.driver.close()

    def read_input_string_from_site(self):
        encodable_string = self.driver.find_element_by_xpath('/html/body/h3').text
        print(encodable_string)
        return encodable_string

    def send_encoded_string_to_site(self, r):
        fieldbox = self.driver.find_element_by_xpath('/html/body/center/form/input[1]')
        fieldbox.clear()
        fieldbox.send_keys(r)
        submit_button = self.driver.find_element_by_xpath('/html/body/center/form/input[2]')
        submit_button.click()
        # sleep(1)
        am_i_slow = self.check_if_i_am_slow()
        if am_i_slow: print('Slowness reported!')

    def check_if_i_am_slow(self):
        try:
            slowness_notification = self.driver.find_element_by_xpath('/html/body/p')
            print(slowness_notification.text)
            r = True
            self.slows += 1
        except:
            r = False
        return r

    def get_slows(self):
        return self.slows