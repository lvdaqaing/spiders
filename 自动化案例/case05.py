# 抓取qq音乐

# 1. 找到音乐文件的下载链接
# http://124.193.228.156/amobile.music.tc.qq.com/C400002E3MtF0IAMMY.m4a?guid=8809189374&vkey=DB083A2D01162AA997731C443A0C0AFE8F1EE4826FE651C0273EEFC11B39A14B0D852BAB5D802CD4AB09BC202C3B8BE9A6A254A4DE326FB9&uin=0&fromtag=66

# 2. 比较不同的歌，分析下载链接的关键词：songmid和vkey

# 3. 寻找vkey在哪个响应里，找到请求网址

# 4. 构造请求网址

import requests,json,re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def download_music(songmid,music_name):
    # url='https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?g_tk=872989112&jsonpCallback=MusicJsonCallback06459212607938936&loginUin=11297258&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8¬ice=0&platform=yqq&needNewCode=0&cid=205361747&callback=MusicJsonCallback06459212607938936&uin=11297258&songmid={0}&filename=C100{0}.m4a&guid=9136027940'.format(songmid)

    # https://u.y.qq.com/cgi-bin/musicu.fcg?callback=getplaysongvkey24583966914882927&g_tk=5381&jsonpCallback=getplaysongvkey24583966914882927&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"8809189374","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"8809189374","songmid":["002E3MtF0IAMMY"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":20,"cv":0}}
    data = json.dumps({"req": {"module": "CDN.SrfCdnDispatchServer", "method": "GetCdnDispatch","param": {"guid": "8809189374", "calltype": 0, "userip": ""}},"req_0": {"module": "vkey.GetVkeyServer", "method": "CgiGetVkey","param": {"guid": "8809189374", "songmid": [songmid], "songtype": [0], "uin": "0", "loginflag": 1,"platform": "20"}}, "comm": {"uin": 0, "format": "json", "ct": 20, "cv": 0}})
    url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?callback=getplaysongvkey32666490664609316&g_tk=5381&jsonpCallback=getplaysongvkey32666490664609316&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data={}'.format(data)
    html= requests.get(url)
    # print(html.text)
    # 去掉jsonp
    music_json= json.loads(re.findall(r'^\w+\((.*)\)$',html.text)[0])
    print(music_json)
    filename=music_json['req_0']['data']['midurlinfo'][0]['filename']
    print(filename)
    vkey=music_json['req_0']['data']['midurlinfo'][0]['vkey']
    # download_url='http://dl.stream.qqmusic.qq.com/{}?vkey={}&fromtag=66'.format(filename,vkey)
    download_url = 'http://111.202.85.144/amobile.music.tc.qq.com/{}?guid=8809189374&vkey={}&uin=0&fromtag=66'.format(filename,vkey)
    # http://111.202.85.144/amobile.music.tc.qq.com/C400002E3MtF0IAMMY.m4a?guid=8809189374&vkey=CB77836DBB8F71AE8B5555F1376B76ABBEA4BA2C517379657E8F98720FC8775EF0A31A41D04FBD095319157FDCFB7904FA0AF2506AC406C9&uin=0&fromtag=66
    # http://111.202.98.144/amobile.music.tc.qq.com/C400002KNcIH2LzRyz.m4a?guid=8809189374&vkey=872B7571195FCB4333F36409767BB65FAAE187DD7EE4D09118220E0F3FC13D55B69C46FA03547E9AE5241EBDA53EBA48E2F5B7B590EB3F81&uin=0&fromtag=66
    print(download_url)

    #下载到本地
    music=requests.get(download_url)
    print('music content =========== ', music.content)
    # print(music.content)
    #文件名去除特殊符号
    with open("/Users/seancheney/Documents/kkb_python/headless/{}.m4a".format(re.sub(r'[\s+|@<>:\\"/]','',music_name)),"wb") as m:
         m.write(music.content)

def view_html():
    # qq音乐页面是js加载的，这里用chrome headless模式访问
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome('/Users/seancheney/Documents/kkb_python/headless/chromedriver',chrome_options=option)

    #排行榜页面
    driver.get('https://y.qq.com/n/yqq/toplist/26.html')
    print(driver.title)
    try:
        # 等待播放列表加载完毕
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "songlist__songname_txt")))

        lis= driver.find_elements_by_class_name('songlist__songname_txt')
        pattern = re.compile(r'https://y.qq.com/n/yqq/song/(\S+).html')
        for i in range(lis.__len__()):
            li = lis.__getitem__(i)
            a= li.find_element_by_class_name('js_song')
            # 获得songid
            href=a.get_attribute('href')
            # print(href)
            music_name=a.get_attribute('title')
            print(music_name)
            m=pattern.match(href)
            # print(m)
            # print(m.group(1))
            download_music(m.group(1),music_name)

    finally:
        driver.quit()


if __name__ == '__main__':
    view_html()