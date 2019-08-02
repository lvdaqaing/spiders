# 模拟登录GitHub

import requests
from lxml import etree


class Login():
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath('//div//input[2]/@value')[0]
        print('authenticity_token =', token)
        return token

    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token(),
            'login': email,
            'password': password
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        print('login status code is:', response.status_code)
        print(response.cookies.get_dict())
        # print(response.url)
        print('response header:', response.request.headers)
        if response.status_code == 200:
            self.repositories_name(response.text)

        response = self.session.get(self.logined_url, headers=self.headers)
        print('profile status code is:', response.status_code)
        if response.status_code == 200:
            self.logo(response.text)

    def repositories_name(self, html):
        selector = etree.HTML(html)
        repositories_name = selector.xpath('//li[contains(@class, "public source")]/div[@class="width-full text-bold"]/a/span[2]/text()')
        print(repositories_name)


    def logo(self, html):
        selector = etree.HTML(html)
        logo_url = selector.xpath('//dl[contains(@class,"form-group")]/dd/img/@src')[0]
        print('logo url is:', logo_url)


if __name__ == "__main__":
    login = Login()
    login.login(email='seancheney@qq.com', password='seancheney123')