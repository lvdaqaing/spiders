# 利用搜狗搜索接口抓取微信公众号

# 搜狗的微信搜索：
# http://weixin.sogou.com
# 搜索：“Python爱好者社区”
# 找到它的微信号：python_shequ

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

option = webdriver.ChromeOptions()
# option.add_argument('headless')

driver = webdriver.Chrome(
    executable_path='/Users/seancheney/Documents/kkb_python/headless/chromedriver',
    chrome_options=option
)

url = 'http://weixin.sogou.com/weixin?type=1&s_from=input&query=python_shequ'

driver.get(url)
print(driver.title)

timeout = 5
link = WebDriverWait(driver, timeout).until(
    lambda d: d.find_element_by_link_text('Python爱好者社区'))
link.click()

import time
time.sleep(1)
# 切换页面
window_handles = driver.window_handles
driver.switch_to.window(window_handles[-1])

print(driver.title)

article_links = WebDriverWait(driver, timeout).until(
    lambda d: d.find_elements_by_xpath('//h4[@class="weui_media_title"]'))
article_link_list = []
for item in article_links:
    article_link = 'https://mp.weixin.qq.com' + item.get_attribute('hrefs')
    # print(article_link)
    article_link_list.append(article_link)

print(article_link_list)

first_article_link = article_link_list[0]

import requests
from lxml import etree

header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

response = requests.get(first_article_link,
                        headers=header,
                        timeout=5
                        )

tree = etree.HTML(response.text)

title = tree.xpath('//h2[@id="activity-name"]/text()')[0].strip()
content = tree.xpath('//div[@id="js_content"]//text()')
content = ''.join(content).strip()

print(title)
print(content)