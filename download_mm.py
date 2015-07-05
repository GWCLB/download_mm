import urllib.request
import re
import os

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36')

    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    
    return html

def get_img(html):
    p = r'<img src="([^"]+\.jpg)'
    imglist = re.findall(p, html)
    '''  
    for each in imglist:
        print(each)
    '''
    for each in imglist:
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each, filename, None)
    
    
def get_page(url):

    html = url
    
    a = html.find("current-comment-page") + 23
    b = html.find("]", a)

    return(html[a:b])
    
def download_mm(folder='OOXX',pages=1):
    os.mkdir(folder)
    os.chdir(folder)
    url = "http://jandan.net/ooxx"
    
    page_num = int( get_page( url_open(url) ) )
    print(page_num)
    
    for i in range(2):
        page_num -= i
        page_url = url + "/page-" + str(page_num) + "#comments"
        get_img(url_open(page_url))
        
    
if __name__ == '__main__':

    download_mm()


    
    
    
    
