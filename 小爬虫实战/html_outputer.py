class HtmlOutputer(object):
    datas=[]
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self,pagename):
        filename="output"+pagename+".html"
        fout = open(filename,"w",encoding="utf-8")
        fout.write("<html>")
        fout.write("<head>")
        fout.write("<meta charset=\"utf-8\">")
        fout.write("</head>")
        fout.write("<body>")
        fout.write("<table style=\"border:1px solid #F00;\">")
        for data in self.datas:
            if len(data["summary"]) < 2 or data["summary"] is None:
                continue
            else:
                fout.write("<tr>")
                #fout.write("<td>%s<td>"%data["url"])
                fout.write("<td style=\"border:1px solid #F00;\">%s<td>"%data["title"])
                fout.write("<td style=\"border:1px solid #F00;\">%s<td>"%data["summary"])
                #print(len(data["summary"]))
                fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()

