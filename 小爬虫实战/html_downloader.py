import urllib3


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        urllib3.disable_warnings()
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
        }
        http = urllib3.PoolManager()
        r = http.request("GET", url,headers=header)
        if r.status != 200:
            return None
        return r.data.decode("utf8")

if __name__=="__main__":
    page = HtmlDownloader()
    print(page.download("https://baike.baidu.com/item/%E6%88%90%E9%83%BD/128473?fr=aladdin"))
