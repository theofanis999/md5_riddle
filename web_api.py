import requests


class web_api:

    def __init__(self, url):
        self.url = url
        self.site_data = None

    def read_input_string_from_site(self):
        if not self.site_data:
            r = self._send_get_req()
            self.set_site_data(r)
        else:
            r = self.site_data
        if ('Too slow!' in r): print('The site says we are Too Slow!!!!!!!!!!!!!!!!')
        p = self._parse_website_for_encodable_string(r)
        # print('\nThe page contains the string {} for us to encode'.format(p))
        return p

    def _send_get_req(self):
        r = requests.get(self.url, headers={'Accept': 'application/json'})
        r1 = r.text
        return r1

    def _parse_website_for_encodable_string(self, r):
        try:
            r1 = r.split("<h3 align='center'>")[1].split("</h3>")[0]
        except:
            print('Cannot find a string to encode in page:\n{}'.format(r))
            r1 = 'NO INPUT'
        # print(r1)
        return r1

    def send_encoded_string_to_site(self, e):
        r = self._send_post_req(e)
        return r

    def _send_post_req(self, postable):
        r = requests.post(self.url, postable)
        page = r.text
        # print('The response page for you to cherish:\n{}\n'.format(page))
        self.set_site_data(page)
        t = self._parse_website_for_encodable_string(page)
        # print('The response page contains the new string {}'.format(t))
        return t

    def set_site_data(self, site_data):
        # try:
        #     print('Site data is:\n{}\n and will now be set to:\n{}'.format(self.site_data, site_data))
        # except:
        #     print('No site data so it will now be set to:\n{}'.format(site_data))
        self.site_data = site_data