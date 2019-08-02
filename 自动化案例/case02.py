# 抓取今日头条的新闻链接

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

option = webdriver.ChromeOptions()
# option.add_argument('headless')

driver = webdriver.Chrome(
    executable_path='/Users/seancheney/Documents/kkb_python/headless/chromedriver',
    chrome_options=option
)

# 今日头条
url = 'https://www.toutiao.com'

driver.get(url)
print(driver.page_source)

timeout = 5
coin_links = WebDriverWait(driver, timeout).until(
    lambda d: d.find_elements_by_xpath('//div[@ga_event="article_title_click"]/a')
)

for item in coin_links:
    print(item.text)
    print(item.get_attribute('href'))