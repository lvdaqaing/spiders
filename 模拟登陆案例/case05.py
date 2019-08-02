# 使用自造的cookies登录马蜂窝

import requests
from lxml import etree

# str = 'mfw_uuid=5bcfcc20-b235-fbbe-c1d6-ae01e1f68d82; _r=baidu; _rp=a%3A2%3A%7Bs%3A1%3A%22p%22%3Bs%3A19%3A%22www.baidu.com%2Fbaidu%22%3Bs%3A1%3A%22t%22%3Bi%3A1540344864%3B%7D; oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222018-10-28+14%3A14%3A32%22%3B%7D; __mfwlv=1540706805; __mfwvn=5; __mfwlt=1540710119; uva=s%3A190%3A%22a%3A4%3A%7Bs%3A13%3A%22host_pre_time%22%3Bs%3A10%3A%222018-10-24%22%3Bs%3A2%3A%22lt%22%3Bi%3A1540344865%3Bs%3A10%3A%22last_refer%22%3Bs%3A64%3A%22https%3A%2F%2Fwww.baidu.com%2Fbaidu%3Ftn%3Dmonline_3_dg%26ie%3Dutf-8%26wd%3Dmafengwo%22%3Bs%3A5%3A%22rhost%22%3Bs%3A13%3A%22www.baidu.com%22%3B%7D%22%3B; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1540344865%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A13%3A%22www.baidu.com%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=5bcfcc20-b235-fbbe-c1d6-ae01e1f68d82; UM_distinctid=166adc88c9b1a0-0e2508b4f33a838-4a506a-1fa400-166adc88c9c6e7; CNZZDATA30065558=cnzz_eid%3D2019380672-1540512335-null%26ntime%3D1540512335; __today_login=1; PHPSESSID=to3oibuiuv9k702m81ui37nes6'

str = 'mfw_uuid=5bcfcc20-b235-fbbe-c1d6-ae01e1f68d82; _r=baidu; _rp=a%3A2%3A%7Bs%3A1%3A%22p%22%3Bs%3A19%3A%22www.baidu.com%2Fbaidu%22%3Bs%3A1%3A%22t%22%3Bi%3A1540344864%3B%7D; __mfwlv=1544535825; __mfwvn=6; __mfwlt=1544537333; uva=s%3A190%3A%22a%3A4%3A%7Bs%3A13%3A%22host_pre_time%22%3Bs%3A10%3A%222018-10-24%22%3Bs%3A2%3A%22lt%22%3Bi%3A1540344865%3Bs%3A10%3A%22last_refer%22%3Bs%3A64%3A%22https%3A%2F%2Fwww.baidu.com%2Fbaidu%3Ftn%3Dmonline_3_dg%26ie%3Dutf-8%26wd%3Dmafengwo%22%3Bs%3A5%3A%22rhost%22%3Bs%3A13%3A%22www.baidu.com%22%3B%7D%22%3B; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1540344865%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A13%3A%22www.baidu.com%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=5bcfcc20-b235-fbbe-c1d6-ae01e1f68d82; UM_distinctid=166adc88c9b1a0-0e2508b4f33a838-4a506a-1fa400-166adc88c9c6e7; CNZZDATA30065558=cnzz_eid%3D2019380672-1540512335-null%26ntime%3D1540512335; oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A20%3A%22passport.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222018-12-11+21%3A43%3A36%22%3B%7D; __today_login=1; uol_throttle=70360114; PHPSESSID=sou2c85ea8lhrirrq8dmaflhf3'

str_list = str.split(';')

# print(str_list)

cookies = {}

for item in str_list:
    # print(item)
    key = item.split('=')[0].strip()
    value = item.split('=')[1].strip()
    cookies[key] = value
print(cookies)




header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

logined_url = 'http://www.mafengwo.cn/friend/index/follow?uid=70360114'
response = requests.get(logined_url, headers=header, cookies=cookies)
print(response.status_code)

tree = etree.HTML(response.text)

friends = tree.xpath('//div[@class="name"]/a/text()')
print(friends)