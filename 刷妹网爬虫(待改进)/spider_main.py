from content_obtain import ContentObtain
from url_manager import UrlManager
from image_down import ImageDown
from html_parser import HtmlParser

class SpiderMain(object):

    def __init__(self):
        self.con = ContentObtain()
        self.uma = UrlManager()
        self.ima = ImageDown('image')
        self.hpa = HtmlParser()

    def start(self,url):
        data = self.hpa.get_html_data(url)
        # 获取性感，清纯，日本，台湾妹子链接 list
        menu_url_lists = self.con.get_content_by_etree(data,'//ul[@id="menu-nav"]/li/a/@href')
        menu_name_lists = self.con.get_content_by_etree(data, '//ul[@id="menu-nav"]/li/a/@title')
        menu_url_lists.pop(0)
        menu_name_lists.pop(0)

        for j in range(0,len(menu_url_lists)):
            #生成链接
            menu_list = url + menu_url_lists[j]

            self.ima.make_dir(menu_name_lists[j])
            # 获取四个分类下总共的页数

            data = self.hpa.get_html_data(menu_list)
            regular = '...</span><a href="'+menu_url_lists[j]+'/(\d{2,})">'

            page = self.con.get_content_by_regular(data,regular)

            for i in range(1,int(page[0])+1):

                #http://www.h666.net/c/xinggan/2
                page_list_url = menu_list+"/"+str(i)

                # 获取页面中15个妹子进入链接
                data = self.hpa.get_html_data(page_list_url)
                item_lists = self.con.get_content_by_etree(data,'//ul[@id="pins"]/li/a/@href')
                item_name_lists = self.con.get_content_by_etree(data,'//ul[@id="pins"]/li/a/img/@alt')
                for i in range(0,len(item_lists)):
                    girl_list = url+item_lists[i]
                    #最终妹子文件夹名字
                    girl_name_dir = self.con.filename_filter(menu_name_lists[j] + '/' + item_name_lists[i])
                    self.ima.make_dir(girl_name_dir)
                    print(girl_list)
                    urls = []
                    urls.append(girl_list)
                    i = 1
                    while len(urls) !=0:
                        data = self.hpa.get_html_data(urls[0])
                        image_url = 'http:' + (self.con.get_content_by_etree(data, '//div/p/a/img/@src'))[0]
                        ima_data = self.hpa.get_image_data(image_url)
                        if ima_data!=0:
                            self.ima.write_image(girl_name_dir + '/' + str(i) + '.png', ima_data)
                        urls.pop(0)
                        i = i+1
                        next_url = self.con.get_content_by_etree(data, '//div[@class="pagenavi"]/a/@href')[-1]
                        url_name = self.con.get_content_by_etree(data, '//div[@class="pagenavi"]/a/span/text()')[-1]

                        if url_name != '下一组»':
                            tmp_url = url + next_url
                            urls.append(tmp_url)


if __name__ == "__main__":
    root_url = 'http://www.h666.net'
    obj_spider = SpiderMain()
    obj_spider.start(root_url)