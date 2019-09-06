import re

from lxml import etree

class ContentObtain(object):

    # 利用etree分析html，得到想要的链接或值
    def get_content_by_etree(self, data, tree):
        xpath_data = etree.HTML(data)
        result = xpath_data.xpath(tree)
        return result

    # 利用正则分析html，得到想要的链接或值
    def get_content_by_regular(self, data, regular):
        pattern = re.compile(regular)
        result = pattern.findall(data)
        return result

    #windows系统中文件名不能包含 \ / : * ? " < > |想要创建必须过滤掉这些字符
    def filename_filter(self,filename):
        filename = re.sub('[:*?"<>|]', '', filename)
        return filename

# 获取性感，清纯，日本，台湾妹子链接 list
 # result = xpath_data.xpath('//ul[@id="menu-nav"]/li/a/@href')

# 获取四个分类下总共的页数
# pattern = re.compile('...</span><a href="/c/xinggan/(\d{2,})">')
# result = pattern.findall(data)

# 获取页面中15个妹子进入链接
# result = xpath_data.xpath('//ul[@id="pins"]/li/a/@href')
# result = xpath_data.xpath('//ul[@id="pins"]/li/a/img/@alt')

# 获取下一图链接
# result = xpath_data.xpath('//div[@class="pagenavi"]/a/@href')[-1]
# 获取“下一组”
# result = xpath_data.xpath('//div[@class="pagenavi"]/a/span/text()')

# 获取每一页的图片http://img.h666.net/image/47/4798/1_368.jpg
# result = xpath_data.xpath('//div/p/a/img/@src')