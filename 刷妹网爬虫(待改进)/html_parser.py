import requests
import time

class HtmlParser(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Connection': 'close'
        }

    #请求网页获取内容
    def get_html_data(self,url):
        response = requests.get(url,headers=self.headers,timeout = 500)
        data = response.content.decode('utf-8')
        response.close()
        return data

    #请求图片返回的内容
    def get_image_data(self,url):
        while 1:
            try:
                r = requests.get(url,headers=self.headers,timeout = 500)
                # print(r.status_code)
                if r.status_code == 200:
                    return r.content
                else:
                    return 0
                r.close()

            except:
                print("Connection refused by the server..")
                print("Let me sleep for 5 seconds")
                print("ZZzzzz...")
                time.sleep(50)
                print("Was a nice sleep, now let me continue...")
                continue