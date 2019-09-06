import os
import re

class ImageDown(object):

    def __init__(self,base_path):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)


    #生成文件夹
    def make_dir(self,path):
        deal_path = './' + self.base_path + '/' + path + '/'
        print(deal_path)
        os.makedirs(deal_path, exist_ok=True)

    #写入图片
    def write_image(self,path,content):
        with open( './' + self.base_path + '/'+path,'wb') as f:
            f.write(content)

# 下载该图片
# os.makedirs('./image/', exist_ok=True)
# r = requests.get('http:'+result[0])
# with open('./image/img2.png', 'wb') as f:
#     f.write(r.content)