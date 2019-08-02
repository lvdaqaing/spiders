# 模拟登录马蜂窝

import requests
from lxml import etree

session = requests.Session()
phone_number = input('电话')
password = input('密码')
data = {'passport': phone_number, 'password': password}
header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
r = session.post("https://passport.mafengwo.cn/login/", headers=header, data=data)
print(r.status_code)
# print(r.text)

logined_url = 'http://www.mafengwo.cn/friend/index/follow?uid=70360114'
response = session.get(logined_url, headers=header)
print(response.status_code)
# print(response.text)

tree = etree.HTML(response.text)

friends = tree.xpath('//div[@class="name"]/a/text()')
print(friends)