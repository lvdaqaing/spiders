# 用selenium实现一个头条号的模拟发文接口

import time
import redis
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


r = redis.Redis('127.0.0.1', 6379)

def toutiao_save_and_preview(title, content, expand_link):
    option = webdriver.ChromeOptions()
    # option.add_argument('headless')
    driver = webdriver.Chrome(executable_path='../chromedriver', chrome_options=option)

    # 获取渲染的正文
    driver.get('file:///Users/seancheney/Documents/kkb_python/headless/cases/paste.html')
    driver.execute_script("contentIn('"+ content +"');")
    timeout = 5
    content_copy = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_xpath('//button[@class="btn"]'))
    content_copy.click()

    # 模拟登录发文页面

    cookie_toutiao = [{'name': 'ccid', 'value': 'db43e70fd9404338c49209ba04f7a11f'}, {'name': 'tt_webid', 'value': '6612748996061414925'}, {'name': 'UM_distinctid', 'value': '1667a53d28d449-0e229246a33996-4a506a-1fa400-1667a53d28e361'}, {'name': 'sso_uid_tt', 'value': '4c8179804d74252717c675607c721602'}, {'name': 'toutiao_sso_user', 'value': '8acc9b248cd201034637248021183d5a'}, {'name': 'sso_login_status', 'value': '1'}, {'name': 'sessionid', 'value': '8441fa3fc5ae5bc08c3becc780b5b2df'}, {'name': '_mp_test_key_1', 'value': '6aba81df9e257bea2a99713977f1e33b'}, {'name': 'uid_tt', 'value': '75b5b52039d4c9dd41315d061c833f0b'}, {'name': 'ccid', 'value': '4231c5cd5a98033f2e78336b1809a18a'}, {'name': 'tt_webid', 'value': '6631884089946523149'}, {'name': 'UM_distinctid', 'value': '16783e1566479-0ae7bcdcaeb592-113b6653-13c680-16783e156656d4'}, {'name': 'passport_auth_status', 'value': '99f731f2c6dc150e6dfea46799f20e90'}, {'name': 'sso_uid_tt', 'value': 'f4bcd2cf972384b428449b0479475ce6'}, {'name': 'toutiao_sso_user', 'value': '60df7bb620b4b6d1d17a1de83daec9c1'}, {'name': 'sso_login_status', 'value': '1'}, {'name': 'sessionid', 'value': '786fe64e9186d51b8427290a557b3c7b'}, {'name': 'uid_tt', 'value': '91a7a72a85861ae686fb66177bc16bca'}, {'name': '__tea_sdk__ssid', 'value': '60b289e6-e2a4-4494-a3e8-7936f9731426'}, {'name': 'uuid', 'value': 'w:3ec91cefd76b438583154fea77baa54b'}, {'name': 'tt_im_token', 'value': '1544105894108419437114683515671344747598423336731147829901779697'}]

    driver.get('https://mp.toutiao.com/profile_v3/index')
    for cookie in cookie_toutiao:
        driver.add_cookie(cookie)
    driver.get('https://mp.toutiao.com/profile_v3/graphic/publish')
    print(driver.title)


    # driver.maximize_window()

    # 写标题
    print('写标题')
    write_title = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_xpath('//*[@id="title"]'))
    write_title.click()
    write_title.send_keys(title)

    # 粘贴正文
    print('写正文')
    write_content = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_xpath(
        '//*[@id="graphic"]/div/div/div[2]/div[1]/div[2]/div[3]/div[2] | //div[contains(@class,"ql-editor")]'))
    write_content.click()
    write_content.clear()
    write_content.send_keys(Keys.SHIFT + Keys.INSERT)
    # time.sleep(1)

    # 检测图片上传是否完成
    try:
        if 'img' in content:
            WebDriverWait(driver, timeout).until(
                lambda d: d.find_element_by_xpath('//div[@class="pgc-img-wrapper"]'))
            print('images uploaded success')
        else:
            print('no image included')
    except:
        print('images uploaded fail')

    # 页面向下滚动
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)

    # 添加扩展链接
    expand_check = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_xpath(
        '//div[@class="pgc-external-link"]//input[@type="checkbox"]',
    ))
    expand_check.click()
    expand_link_box = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_xpath(
        '//div[@class="link-input"]//input[@type="text"]',
    ))
    expand_link_box.send_keys(expand_link)
    time.sleep(1)

    # 自动封面
    front_img = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_xpath(
        '//div[@class="article-cover"]/div/div[@class="tui2-radio-group"]/label[3]/div/input',
    ))
    front_img.click()
    time.sleep(1)

    # 保存草稿
    save_draft = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_xpath(
        '//div[@class="publish-footer"]/button[4]/span'))
    save_draft.click()
    time.sleep(1)

    # 从内容管理页，获取预览链接和文章ID
    print('get preview_link and article_id')
    # driver.refresh()
    preview_link = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_xpath(
        '//div[@id="article-list"]//div[@class="master-title"][1]/a')).get_attribute('href')
    article_id = preview_link.split('=')[-1]
    print(preview_link, article_id)
    time.sleep(1)


    content_management = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_link_text('内容管理'))
    content_management.click()
    time.sleep(1)
    driver.refresh()
    preview_link = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_xpath(
        '//*[@id="article-list"]/div[2]/div/div/div[1]/div/a')).get_attribute('href')
    article_id = preview_link.split('=')[-1]

    index_page = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_xpath('//a[@class="shead_logo"]'))
    index_page.click()
    driver.get('https://mp.toutiao.com/profile_v3/index')

    print(r.scard('cookie_pool_toutiao'))
    return preview_link, article_id


if __name__ == "__main__":
    print('start')
    start_time = time.time()
    title = '狮子王 Circle of Life 345'
    content = '<p>奥术大师多</p><p><img class="wscnph" src="https://upload-images.jianshu.io/upload_images/7178691-a023399f84034497.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/528" /></p>'
    expand_link = 'https://www.jianshu.com/u/130f76596b02'
    img = ''
    preview_link, article_id = toutiao_save_and_preview(title, content, expand_link)
    print(preview_link)
    print(article_id)
    finish_time = time.time()
    print(finish_time - start_time)