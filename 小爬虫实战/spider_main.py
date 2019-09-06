from seachweb import url_manager,html_downloader,html_parser,html_outputer
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    def craw(self, root_url):
        count = 1
        pagename="文件名"
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("正在抓取第%d个页面,链接地址为：%s"%(count,new_url))
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                if new_url==root_url:
                    print(new_data["title"])
                    pagename=new_data["title"]
                #print(new_data)
                self.urls.add_new_urls(new_urls)
                print("已将%d个链接放入地址池"%(len(self.urls.new_urls)))
                print(self.urls.new_urls[0:2])
                print(len(self.urls.old_urls))
                self.outputer.collect_data(new_data)
                if count == 20:
                    break
                count = count+1
            except:
                print("失败")
        self.outputer.output_html(pagename)


if __name__=="__main__":
    root_url="https://baike.baidu.com/item/%E9%82%93%E5%B0%8F%E5%B9%B3/116181"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
