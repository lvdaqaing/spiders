import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from seachweb.html_downloader import HtmlDownloader


class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        #new_urls = set()
        new_urls = []
        #list_urls=[]
        links = soup.find_all("a", href=re.compile(r"^/item/\W+[^#?]*"))
        for link in links:
            new_url = link.get("href")
            new_full_url = urljoin(page_url,new_url)
            new_urls.append(new_full_url)
            #list_urls.append(new_full_url)
        return new_urls#,list_urls


    def _get_new_data(self, page_url, soup):
        res_data={}
        res_data["url"] = page_url
        title_node = soup.find("h1")
        res_data["title"]=title_node.string
        summary_node = soup.find(class_="lemma-summary")
        summarytext = summary_node.get_text()
        summarytext = re.sub(r"\[\w+\]|\[\w+-\w+\]", "", summarytext)
        res_data["summary"] = summarytext
        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,"html.parser")
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data
if __name__=="__main__":
    url="https://baike.baidu.com/item/%E5%B9%BF%E5%AE%89/16896"
    page = HtmlDownloader()
    res=HtmlParser()
    sup=page.download(url)
    data=res.parse(url,sup)
    print(len(data[0]))
    for link in data[0]:
        print(link)
