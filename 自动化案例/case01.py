# 与百度首页交互

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

option = webdriver.ChromeOptions()
# option.add_argument('headless')

# 要换成适应自己操作系统的chromedriver
driver = webdriver.Chrome(
    executable_path='/Users/seancheney/Documents/kkb_python/headless/chromedriver',
    chrome_options=option
)


url = 'https://www.baidu.com'

# 打开网站
driver.get(url)

# 打印当前页面标题
print(driver.title)

# 在搜索框中输入文字
timeout = 5
search_content = WebDriverWait(driver, timeout).until(
    # lambda d: d.find_element_by_xpath('//input[@id="kw"]')
    EC.presence_of_element_located((By.XPATH, '//input[@id="kw"]'))
)
search_content.send_keys('python')

import time
time.sleep(3)

# 模拟点击“百度一下”
search_button = WebDriverWait(driver, timeout).until(
    lambda d: d.find_element_by_xpath('//input[@id="su"]'))
search_button.click()

# 打印搜索结果
search_results = WebDriverWait(driver, timeout).until(
    # lambda d: d.find_elements_by_xpath('//h3[@class="t c-title-en"] | //h3[@class="t"]')
    lambda e: e.find_elements_by_xpath('//h3[contains(@class,"t")]/a[1]')
)
# print(search_results)

for item in search_results:
    print(item.text)

driver.close()