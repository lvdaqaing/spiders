import requests
from lxml import etree

def load_butian():
    url = 'https://www.butian.net/Loo/index/p/10.html'
    loop_lists = []
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'PHPSESSID=5hpsjf4cemu3p9tavhll1mmko1; __DC_sid=66782632.644858303760433500.1562571631637.1926; __guid=66782632.4074614707798417400.1562571631642.066; _currentUrl_=%2FLoo%2Findex%2Fp%2F1.html; __q__=1562572361605; __DC_monitor_count=32; __DC_gid=66782632.555183640.1562571631641.1562572364106.67',
        'Host': 'www.butian.net',
        'Referer': 'https://www.butian.net/Loo/index/p/6002.html',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    data = response.content.decode()

    xpath_data = etree.HTML(data)

    loop_list = xpath_data.xpath('//ul[@class="loopListBottom"]/li/dl/dd[1]')

    for loop in loop_list:
        if loop.xpath('.//span[1]/text()')[0] == '带头大哥':
            if loop.xpath('.//span[3]/text()') == []:
                loop_lists += loop.xpath('.//a/text()')
                print(loop.xpath('.//a/text()'))
            else:
                loop_lists += loop.xpath('.//span[3]/text()')
                print(loop.xpath('.//span[3]/text()'))

        if loop.xpath('.//span[1]/text()')[0] == '发现了':
            loop_lists += loop.xpath('.//span[2]/text()')

    print(len(loop_lists))

load_butian()