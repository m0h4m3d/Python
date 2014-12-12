import urllib.request
from urllib.error import  URLError
import re
from datetime import datetime


def visit_url(url, domain):
    crawler_backlog = {}
    crawler_backlog[url]=0
    if(len(crawler_backlog)>100):
        return
    if(url in crawler_backlog and crawler_backlog[url] == 1):
        return
    else:
        crawler_backlog[url] = 1
        print("Processing:", url)
    try:
        page = urllib.request.urlopen(url)
        code=page.getcode()
        if(code == 200):
            content=page.read()
            content_string = content.decode("utf-8")
            regexp_para = re.compile('<p>(?P<p>(.*))</p>')
            regexp_keywords = re.compile('<meta name="keywords" content="(?P<keywords>(.*))" />')
            regexp_url = re.compile("http://"+domain+"[/\w]*")
            result = regexp_para.search(content_string, re.IGNORECASE)
            if result:
                p = result.group("p")
                data_list = p.split(".")
            result = regexp_keywords.search(content_string, re.IGNORECASE)
            if result:
                keywords = result.group("keywords")
                data_list.append(keywords)
            for (urls) in re.findall(regexp_url, content_string):
                if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
                    crawler_backlog[urls] = 0
                    visit_url(urls, domain)
            return data_list
    except URLError as e:
        print()


def webParserData():
    seed = "http://en.wikipedia.org"
    web_data = visit_url(seed,"en.wikipedia.org")
    return data_list
