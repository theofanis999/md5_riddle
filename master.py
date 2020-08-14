from encoder import encoder
from web_api import web_api
from selenium_api import selenium_api
from time import sleep

URL = 'http://docker.hackthebox.eu:32032/'
USE_SELENIUM = True
REPETITIONS = 100
PAUSE = 0

class master:

    def __init__(self, url):
        self.encoder = encoder()
        self.webapi = web_api(url)
        self.seleapi = selenium_api(url)


    def do_everything(self, with_selenium=False):
        # if with_selenium:
        #     self.seleapi.go_to_page()
        s = self.read_string(with_selenium)
        e = self.encode_string(s)
        # sleep(PAUSE)
        r = self.submit_encoded_string(e, with_selenium)
        # self.print_response(s, e, r)
        # if with_selenium:
        #     self.seleapi.close_browser()

    def read_string(self, with_selenium=False):
        if with_selenium:
            r = self.seleapi.read_input_string_from_site()
        else:
            r = self.webapi.read_input_string_from_site()
        # print(r)
        return r

    def encode_string(self, s):
        e = self.encoder.md5_encode_string(s)
        return e

    def submit_encoded_string(self, e, with_selenium=False):
        if with_selenium:
            r = self.seleapi.send_encoded_string_to_site(e)
        else:
            r = self.webapi.send_encoded_string_to_site(e)
        return r

    def print_response(self, s, e, r):
        print('The response to submitting string "{}" encoded as "{}" was the new string:\n{}'.format(s, e, r))

    @staticmethod
    def wait(t):
        if t != 0:
            tt = 0
            while tt <= t:
                print(tt)
                tt += 1
                sleep(1)
            print('\n')


if __name__ == '__main__':
    myMa = master(URL)
    i = REPETITIONS
    while i > 0:
        print('\n\n======\nATTEMPT #{}\n'.format(REPETITIONS-i+1))
        if USE_SELENIUM:
            myMa.seleapi.go_to_page()
        myMa.do_everything(USE_SELENIUM)
        i -= 1
    print('The slow score was {}/{}'.format(myMa.seleapi.get_slows(), REPETITIONS))
    if USE_SELENIUM:
        myMa.seleapi.close_browser()


